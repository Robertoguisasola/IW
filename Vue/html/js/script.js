// Initialize Firebase

const config = {
  apiKey: "AIzaSyCzRLn1728CWTieyKk0AwXX6eUTN-kspk0",
  authDomain: "agenda-c92a9.firebaseapp.com",
  databaseURL: "https://agenda-c92a9.firebaseio.com/",
  storageBucket: "gs://agenda-c92a9.appspot.com",
  messagingSenderId: "397822333249"
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

    // ContactoRef.once('value')
    //   .then((value) => {
    //     let users = Object.values(value.val());
    //     users.forEach((user) => {
    //       contactos.push(user);
    //     });
    //   });

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
