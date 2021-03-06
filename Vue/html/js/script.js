const config = {
  apiKey: "AIzaSyDzX625bRue00McJQJ9ZcPKYp5nXPnfNcs",
  authDomain: "ski-stick.firebaseapp.com",
  databaseURL: "https://ski-stick.firebaseio.com/",
  storageBucket: "gs://ski-stick.appspot.com",
  messagingSenderId: "1009221022071"
};
let app = firebase.initializeApp(config);
let db = app.database();
let ContactoRef = db.ref('Contactos');

let vue = new Vue({
  el: '#app',
  data: {
    nombre: "",
    email: "",
    telefono: "",
    contactos: []
  },
  mounted: function () {
    let contactos = this.contactos;
    ContactoRef.once('value')
    .then((value) => {
      let values = value.val();
      let userKeys = Object.keys(values);
      let users = Object.values(values);
      users.forEach((user, i) => {
        user.key = userKeys[i];
        contactos.push(user);
      });
    });
  },
  firebase: {
    contactos: ContactoRef
  },
  methods: {
    añadir: function (e) {
      e.preventDefault();
      if (this.nombre && this.email && this.telefono) {
        ContactoRef.push({
          nombre: this.nombre,
          email: this.email,
          telefono: this.telefono,
        });
        this.contactos.push({
          nombre: this.nombre,
          email: this.email,
          telefono: this.telefono,
        });
        this.nombre = '';
        this.email= '';
        this.telefono = '';
        
      }else{
        document.getElementById("missing-fields-alert").className = "";
      }

    },
    borrar: function (e, contacto) {
      e.preventDefault();
      this.contactos.splice(this.contactos.indexOf(contacto), 1);
      ContactoRef.child(contacto.key).remove();
            
    }    
  },
});
