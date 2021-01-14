function Tooltip(el, text) {
            /*
               This function is used to trigger the tooltip box if the hovering is done over question mark 
               icon whose classlist includes tool 
            */

            el.onmouseover = function () {
                console.dir(el)
                // Adding the below html to the existing one so that tooltip window appears
                el.innerHTML += '<div class="tooltip">' + text + '</div>'
            }
            el.onmouseout = function () {
                // on removing the mouse pointer the tooltip box will go away 
                el.removeChild(el.querySelector(".tooltip"))
            }
        }

        //Below is the function which will be called with the required text
        Tooltip(document.getElementById('tool'), "Only alphanumeric,hyphen(-),underscore(_) allowed. Spaces not allowed.")