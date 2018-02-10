from flask import Flask
app = Flask(__name__)


class Fish(Resource):
    
    def get_fish(feed_name):
        fish_list = []
        fish_that_eat_feed = Fish.query.filter_by(feed_name=feed_name).all()
        if fish_that_eat_feed:
           for fish in fish_that_eat_feed:
               fish_details = {
                    'id': fish.id,
                    'name': fish.name
                }
                fish_list.append(fish_details)

            return jsonify({'fish that eat feed are': fish_list}, 200)
        else:
            return("no fish that eat that feed at the moment!")


class Feeds(Fish):
    def get_feed(feed_name):
        feed_name = Feed.query.filter_by(name=feed_name).first()
        if feed_name:
            impact = Feed.query.filter_by(feed_name=feed_name).first()
            suppliers = get_supliers.feed_suppliers
            feed_id = Feed.query.filter_by(feed_name=feed_name).first()
            Fishes = Fish.Fish_list
        else:
            return("no feeds by that name yet!")

    def get_suppliers(feed_name):
        feed_suppliers = []
        suppliers = Supplier.query.filter_by(feed_name=feed_name).all()
        if suppliers:
            for supplier in suppliers:
                supplier_details = {
                    'id': supplier.id,
                    'name': supplier.name
                    'telephone' = supplier.telephone,
                    'price' = supplier.price # bug from database models
                    'feed_id' = supplier.feed_id
                }
                feed_suppliers.append(supplier_details)

            return jsonify({'suppliers': feed_suppliers}, 200)
        else:
            return("no suppliers for that at the moment!")


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()




                




            
