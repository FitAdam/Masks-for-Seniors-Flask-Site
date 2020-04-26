from mask_site import create_app
#from mask_site import db
app = create_app()

if __name__ == "__main__":
    #db.drop_all()
    #db.create_all()
    app.run()


      
    