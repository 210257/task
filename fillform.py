import requests

url = "http://localhost/form.php"
r = requests.post(url, data={"name":"shyam",
                             "email":"shyam@shyam.com",
                             "submit": "Submit"})
print(r.text)