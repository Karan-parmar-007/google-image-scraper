from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import logging
import pymongo
logging.basicConfig(filename="scrapper.log" , level=logging.INFO)
import os

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def homepage():
    return render_template("index.html")

@app.route("/review" , methods = ['POST' , 'GET'])
def index():
    if request.method == 'POST':
                try:

                    # query to search for images
                    query = request.form['content'].replace(" ","+")

                            # directory to store downloaded images
                    save_directory = "images/"

                            # create the directory if it doesn't exist
                    if not os.path.exists(save_directory):
                        os.makedirs(save_directory)



                            # fake user agent to avoid getting blocked by Google
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

                            # fetch the search results page
                    response = requests.get(f"https://www.google.com/search?sca_esv=64193000b358b41f&rlz=1C1ONGR_enIN1065IN1065&sxsrf=ADLYWIKENiCswXBy1_EI76visxN740s3OQ:1717300627428&q={query}&uds=ADvngMhdvWgwd1DARqoW4xZQ2piG0uI_v_aZNZYD9zXcyhLjV0BWuExabQOnwjUSZSEClPBRnpmRxn9CJm3uROsGl7j-OKVTFsMqTksrJGeAXojSaKaBOu05ma3n6qJ8k0aKcMiqJjQGcYyVR5Sq_-Zd-ZoOmtgMzQrzfTG2z3IkT-5_3gGTD7Ipa2SEVV9rknSYwd2FbCtCusbLr8ID-5HtVINzhRXPtuYAXXxy1NVetpCcndnVNZK4SXOoNIrELtmvzgleiYNmDorE5uVLZEpHOC-cJ5JGmu0Pqg3B77OzK6T2iO49kZqg_Wi_QMPOQW2wdxfe1pMT&udm=2&prmd=nivsmbtz&sa=X&ved=2ahUKEwiG8Pqug7yGAxUCTWwGHc6HAtYQtKgLegQIEBAB&biw=724&bih=649&dpr=1.32")


                            # parse the HTML using BeautifulSoup
                    soup = BeautifulSoup(response.content, "html.parser")

                            # find all img tags
                    image_tags = soup.find_all("img")

                            # download each image and save it to the specified directory
                    del image_tags[0]
                    img_data=[]
                    for index,image_tag in enumerate(image_tags):
                                # get the image source URL
                                image_url = image_tag['src']
                                #print(image_url)
                                
                                # send a request to the image URL and save the image
                                image_data = requests.get(image_url).content
                                mydict={"Index":index,"Image":image_data}
                                img_data.append(mydict)
                                with open(os.path.join(save_directory, f"{query}_{image_tags.index(image_tag)}.jpg"), "wb") as f:
                                    f.write(image_data)
                    client = pymongo.MongoClient("mongodb+srv://pw_course:pw_course@cluster0.amara6i.mongodb.net/?retryWrites=true&w=majority")
                    db = client['image_scrap']
                    review_col = db['image_scrap_data']
                    review_col.insert_many(img_data)          

                    return "image laoded"
                except Exception as e:
                    logging.info(e)
                    return 'something is wrong'
            # return render_template('results.html')

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
