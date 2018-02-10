from flask import Flask
app = Flask(__name__)


class Fish(Resource):
    
    def get_fish(feed_name):
        Fish_list = []
        fish_that_eat_feed = Fish.query.filter_by(feed_id=).all()
        if fish_that_eat_feed:
           for fish in fish_that_eat_feed:
               Fish_list.append(fish)
        else:
            print("no fish that eat that feed at the moment!")



class Feeds(Fish):
    def get_feed(feed_name):
        feed_name = Feed.query.filter_by(name=feed_name).first()
        if feed_name:
            impact = Feed.query.filter_by(feed_name=feed_name).first()
            suppliers = get_suupliers.feed_suppliers
            Fishes = Fish.Fish_list

    def get_suppliers(feed_name):
        feed_suppliers = []
        suppliers = Supplier.query.filter_by(feed_name=feed_name).all()
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




                




            
