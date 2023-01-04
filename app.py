from flask import Flask, render_template, request

def validate_all(property, *keys: tuple[str]):

    validated = [True if key in keys else False for key in keys]
    return all(validated)


class App(Flask):
    def __init__(self):
        super().__init__(__name__)

        self.__build_routes()
        self.run()
    
    def __build_routes(self):

        # HOMEPAGE
        @self.route("/", methods=["POST", "GET"])
        def homepage():

            request_method = request.method

            weight = 0
            height = 1

            bmi = (weight) / (height ** 2)
            bmi = round(bmi, 2)

            if ((validate_all(request.form, "height", "weight")) and (request_method == "POST")):
                weight = float(request.form.get("weight"))
                height = float(request.form.get("height"))
            
            bmi = (weight) / (height ** 2)
            bmi = round(bmi, 2)


            return render_template("index.html", bmi=bmi)


if __name__ == "__main__":
    App()