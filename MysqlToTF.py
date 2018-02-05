#sudo apt-get install libmysqlclient-dev
#pip install mysqlclient
import csv
import MySQLdb
import tensorflow as tf

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root')
cursor = mydb.cursor()

#list of db's
dbs = ['mysql']
#table name
table_name = "user"
count = 0
for i in dbs:
## query
    query = ("SELECT * FROM "+i+"."+table_name)
    cursor.execute(query)

### write to csv file
    csv_writer = csv.writer(open(i+".csv", "wt")) # create csv
    csv_writer.writerow([i[0] for i in cursor.description]) # write headers
    csv_writer.writerows(cursor) # write records
    del csv_writer # close csv file
    print("Query executed for "+i)
    print("Wrote %s rows to csv." % cursor.rowcount)
    count = len(cursor.description)

cursor.close()
mydb.close()

filename_queue = tf.train.string_input_producer(
    [dbs[0]+".csv"],
    shuffle=True)

# Each file will have a header, we skip it and give defaults and type information
# for each column below.
line_reader = tf.TextLineReader(skip_header_lines=1)

_, csv_row = line_reader.read(filename_queue)

# Type information and column names based on the decoded CSV.
#record_defaults = [[0.0], [0.0], [0.0], [0.0], [""]]
record_defaults = [["" for col in range(1)] for row in range(count)]
a = tf.decode_csv(csv_row, record_defaults=record_defaults)

# Turn the features back into a tensor.
features = tf.stack(a[0:count])

with tf.Session() as sess:
    tf.initialize_all_variables().run()

    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    # We do 10 iterations (steps) where we grab an example from the CSV file. 
    for iteration in range(1, 11):
        # Our graph isn't evaluated until we use run unless we're in an interactive session.
        example = sess.run([features])

        print(example)
coord.request_stop()
coord.join(threads)
