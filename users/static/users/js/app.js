const setupApp = ()=>{
    hookUpBtns();
}

function hookUpBtns(){
    const lineStartings = [0,20,40,60,80];
    const pageStartings = [0,-100,-200,-300,-400];
    const underline = document.querySelector(".underline");
    const btns = document.querySelectorAll(".navicon");
    const home = document.querySelector('.home');
    const search = document.querySelector('.search');
    const connect = document.querySelector('.connect');
    const messages = document.querySelector('.messages');
    const profile = document.querySelector('.profile');
    const editMenu = document.querySelector('.edit-menu');
    const editMenuBtn = document.querySelector('.edit');
    const crossSignEdit = document.querySelector('.cross-sign');
    const overlay = document.querySelector('.overlay-background');
    const bronektBtn = document.querySelector('.bronekt-btn');
    const newFeedsContainer = document.querySelector('.newfeeds-container');
    const editInputs = document.querySelectorAll('.edit-input');
    const insertPhotoBtn = document.getElementById('insert-photo-icon');
    const recordBtn = document.getElementById('recording-mic-btn');
    const insertAudio = document.getElementById('insert-sound-icon');
    const crossNotationMic = document.querySelector('.cross-notation-mic');
    const shareBtn = document.querySelector('.share');
    const shareMenu = document.querySelector('.share-menu');
    const crossSignShare = document.getElementById('cross-sign-share');
    const copyProfileLinkBtn = document.getElementById('copy-profile-link');




    copyProfileLinkBtn.addEventListener('click',()=>{
        const link = document.getElementById('share-link');
        link.select();
        link.setSelectionRange(0,99999);
        document.execCommand('copy');
    });




    crossSignShare.addEventListener('click',()=>{
        shareMenu.classList.toggle('menu-hider');
        shareMenu.classList.toggle('menu-shower');
        overlay.classList.toggle('over-active');
    });

    shareBtn.addEventListener('click',()=>{
        shareMenu.classList.toggle('menu-shower');
        shareMenu.classList.toggle('menu-hider');
        overlay.classList.toggle('over-active');
    });


    crossNotationMic.addEventListener('click',()=>{
        const micMenuBlob = document.getElementById('mic-blob');
        micMenuBlob.classList.toggle('mic-blob-disappear');
    });

    insertAudio.addEventListener('click',()=>{
        const micMenuBlob = document.getElementById('mic-blob');
        micMenuBlob.classList.toggle('mic-blob-disappear');
    });



    recordBtn.addEventListener('touchstart',()=>{
        recordBtn.style.color = 'rgb(228, 47, 47)';

    },false);

    recordBtn.addEventListener('touchend',()=>{
        recordBtn.style.color = 'rgb(119, 119, 119)';
    },false);

    insertPhotoBtn.addEventListener('click',()=>{
        const inputPhoto = document.getElementById("insert-img-btn");
        inputPhoto.click();
    });


    editInputs.forEach((elem)=>{
        
        try{

            elem.addEventListener('change',()=>{
                elem.parentElement.getElementsByTagName('label').item(0).innerText = 
                elem.value;
                elem.value = '';
            });
        }catch(error){}
    });

    bronektBtn.addEventListener('click',()=>{
        const bronektComposingArea = document.getElementById('brocode-composing-area');
        if(bronektComposingArea.value.length>0){
            const brocode = createNewBrocode(bronektComposingArea.value);
            bronektComposingArea.value='';
            newFeedsContainer.insertAdjacentHTML('afterbegin',brocode);
        }
    });
    
    crossSignEdit.addEventListener('click',()=>{
        editMenu.classList.toggle('menu-hider');
        editMenu.classList.toggle('menu-shower');
        overlay.classList.toggle('over-active');


    });
    editMenuBtn.addEventListener('click',()=>{
        editMenu.classList.toggle('menu-shower');
        editMenu.classList.toggle('menu-hider');
        overlay.classList.toggle('over-active');
    });
    
    var prevScrollpos = 0;
    profile.addEventListener('scroll',()=>{
        if (profile.scrollTop >= 0){
            var currentScrollPos = profile.scrollTop;
            if (prevScrollpos < currentScrollPos) {
                document.querySelector(".navigation-list").style.bottom = "-50px";
                document.querySelector(".underline").style.bottom = "-50px";
            } else {
                document.querySelector(".navigation-list").style.bottom = "0px";
                document.querySelector(".underline").style.bottom = "0px";
            }
            prevScrollpos = currentScrollPos;
        }
    });


    home.addEventListener('scroll',()=>{
        if (home.scrollTop >= 0){
            var currentScrollPos = home.scrollTop;
            if (prevScrollpos < currentScrollPos) {
                document.querySelector(".navigation-list").style.bottom = "-50px";
                document.querySelector(".underline").style.bottom = "-50px";
            } else {
                document.querySelector(".navigation-list").style.bottom = "0px";
                document.querySelector(".underline").style.bottom = "0px";
            }
            prevScrollpos = currentScrollPos;
        }
    });

    for(let i = 0;i<btns.length;i++){
        btns[i].addEventListener('click',()=>{
            underline.style.left = `${lineStartings[i]}%`
            btns[i].style.color = 'rgb(228, 47, 47)';
            home.style.transform = `translateX(${pageStartings[i]}vw)`;
            search.style.transform = `translateX(${pageStartings[i]}vw)`;
            connect.style.transform = `translateX(${pageStartings[i]}vw)`;
            messages.style.transform = `translateX(${pageStartings[i]}vw)`;
            profile.style.transform = `translateX(${pageStartings[i]}vw)`;

            for(let j = 0;j<btns.length;j++){
                if(j!==i){
                    btns[j].style.color = 'rgb(119, 119, 119)';
                }
            }
        });
    }
}

function createNewBrocode(brocode){
    brocode = brocode.replace(/\n/g,'<br>');
    let brocodeTemplate = `<div class="tweet">
    <div class="tweet-container-left-col">
        <div class="tweet-author-picture-container">
            <img src="https://holmesbuilders.com/wp-content/uploads/2016/12/male-profile-image-placeholder.png" alt="" class="profile-header-img">
        </div>
    </div>
    <div class="tweet-container-right-col">
        <div class="tweet-card-header">
            <div class="tweet-author-display-name">User</div>
            <div class="tweet-author-username">@Username</div>
        </div>     
        <div class="tweet-content">
            <p class="tweet-content-p">${brocode}</p>
        </div>
        <ul class="brocodes-action-btns">
            <li class="brocode-action-btn"><span class="material-icons action-icon">reply</span></li><!--
            --><li class="brocode-action-btn"><span class="material-icons action-icon">thumbs_up_down</span></li><!--
            --><li class="brocode-action-btn"><span class="material-icons action-icon">favorite</span></li><!--
            --><li class="brocode-action-btn"><span class="material-icons action-icon">share</span></li>
        </ul>
    </div>
 </div>`;

    return brocodeTemplate;
}

window.onload = setupApp;
