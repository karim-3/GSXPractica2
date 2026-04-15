from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import psycopg2 

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        db_status = "No connectat"
        try:
            # Intentem connectar al servei 'db' definit al compose
            conn = psycopg2.connect(
                host="db", 
                database="greendev_db",
                user="gsx_user",
                password=os.getenv('DB_PASSWORD')
            )
            conn.close()
            db_status = "Connexió a la DB d'establerta amb èxit!"
        except Exception as e:
            db_status = f"Error de connexió: {str(e)}"
        
        self.send_response(200)
        self.end_headers()
        response = f"Hello from GreenDevCorp!\nEstat de la xarxa interna: {db_status}"
        self.wfile.write(response.encode())

server = HTTPServer(('0.0.0.0', 3000), handler)
print("Servidor corrent al port 3000...")
server.serve_forever()