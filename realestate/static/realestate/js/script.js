



$(document).ready(function(){


    $('#menu').kendoMenu({

        dataSource: [
            {
                text: "Buy",
                url: "/"
            },
            {
                text: "Sell",
                url: "/sell_property/"
            },
            {
                text: "Home Loan"
            },
            {
                text: "Become a Seller",
                url: "/signup_view/"
            }
        ]
    })

    $('#menu2').kendoMenu({

        dataSource: [
            {
                text: "Login",
                url: "/signin_view/"
            }
        ]
    })

    $('#s-menu').kendoMenu({

        dataSource: [
            {
                text: "Buy",
                url: "/"
            },
            {
                text: "Sell",
                url: "/sell_property/"
            },
            {
                text: "Home Loan"
            },
            {
                text: "Edit Profile",
                url: "/profile_view/?edit=1"
            } 
        ]
    })

    $('#s-menu2').kendoMenu({

        dataSource: [
            {
                text: "Logout",
                url: "/logout/"
            }
            
        ]
    })

    $('.date').kendoDatePicker({
        format: "yyyy-MM-dd"

    });

    $('.combo-box').kendoDropDownList();

    $('.upload-file').kendoUpload({
        remove: onFileInputRemove,
        select: onFileInputSelect
    });


    let originalURL = $('#profile-pic').attr('src');

    function onFileInputSelect(e){

        console.log('onchange fired on image-input');

        let reader = new FileReader();
        // inputElement = e.target;

        reader.onload = function(e){

            $('#profile-pic').attr('src', e.target.result);
        }

        reader.readAsDataURL(e.files[0].rawFile);


    };

    function onFileInputRemove(e){

        console.log('remove fired on image-input');
        console.log(e.files.length);
        if (e.files.length === 1){
            $('#profile-pic').attr('src', originalURL);
            return;
        }
            
            

        let reader = new FileReader();
        // inputElement = e.target;

        reader.onload = function(e){

            $('#profile-pic').attr('src', e.target.result);
        }

        reader.readAsDataURL(e.files[e.files.length - 1].rawFile);


    };


    var dialog = $("#change-password-dialog");
    dialog.kendoDialog({
        width: "450px",
        visible: false,
        title: "Change Your Password",
        closable: true,
        modal: true,
        // content:"",
        actions: [
            {
                text: 'Change Password',
                primary: true,
                action: function (){
                    let form = $('#change_password_form')[0];
                    console.log(form);

                    let formData = new FormData(form);

                    fetch(form.action, {
                        method: 'POST',
                        body: formData,
                    })
                    // .then(function (respone){
                    //     return Response.json()
                    // })
                    .then((response) => response.json())
                    .then((data) => {
                        alert('password changed.');
                    })
                    .catch((error) => {
                        alert('password change failed.', error);
                    }); 
                    

                    //process fetch response
                    console.log('fetch request sent');
                }
            }
        ],
        close: onClose  
    });
    var changeButton = $("#change-password-button");

    changeButton.click(function () {
        dialog.data("kendoDialog").open();
        changeButton.fadeOut();
    });

    function onClose() {
        changeButton.fadeIn();
    }
    
    
});


