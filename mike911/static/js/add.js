var counter = 2;
        function add(){
            var asd = document.createElement('br')
            var input = document.createElement('input');
            var label = document.createElement('label');

            input.name = 'fild' + counter;
            input.type = "text";
            input.id = "fild" + counter;
            label.setAttribute("for","fild" + counter);
            label.innerHTML = "fild_" + counter + ":&nbsp";
            
            document.getElementById('form-group').appendChild(label);
            document.getElementById('form-group').appendChild(input);
            document.getElementById('form-group').appendChild(asd);
            
            counter++;
            
        }