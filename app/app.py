from flask import Flask
app = Flask(__name__)


class Fish(Resource):
    
    def get_fish(feed_id):
        Fish_list = []
        fish_that_eat_feed = # fish with feed ID query from the database
        if fish_that_eat_feed:
           for fish in fish_that_eat_feed:
               Fish_list.append(fish)
        else:
            print("no fish that eat that feed at the moment!")



class Feeds(Fish):
    def get_feed(feed_name):
        feed_name = BucketList.query.filter_by(id=ID).first()
        if feed_name:
            impact = BucketListItem.query.filter_by(bucket_list_it_belongs_to=bucketlist.name).all()
            feed_id = BucketListItem.query.filter_by(bucket_list_it_belongs_to=bucketlist.name).all()
            suppliers = get_suupliers.feed_suppliers
            Fishes = Fish.Fish_list

def get_suppliers(feed_id):
        feed_suppliers = []
        suppliers = # supplier with feed ID query from the database
        if suppliers:
            for supplier in suppliers:
                feed_suppliers.append(supplier)
        else:
            print("no suppliers for that at the moment!")


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()




                




            
