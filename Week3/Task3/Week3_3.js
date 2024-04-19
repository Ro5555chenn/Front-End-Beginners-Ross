fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
    .then(response => {
        return response.json(); 
    })
    .then(data => {
        spotList = data.data.results;
        for (let i = 0; i < 13; i++) { 
            const spot = spotList[i];
            const title = spot.stitle;
            const imageURL = spot.filelist;
            const image = imageURL.split("https://").slice(1);
            const imageFirst ="https://"+ image[0];

            

            const block = document.querySelector(".block");
            const NewBox = document.createElement("div");
            if(i<3){
                NewBox.className = "box-1";
            }else if(i%10 ===3 || i%10 ===8 ){
                NewBox.className = "box-2";
            }else{
                NewBox.className = "box-3";
            }

            if (i === 2){
                NewBox.id = "box-rwd"; 
            }else if(i === 11 || i ===12 ){
                NewBox.id = "box-rwd-2";
            }

            const Newpic1 = document.createElement("div");
            if(i<3){
                Newpic1.className = "pic-1";
            }else if(i%10 ===3 || i%10 ===8 ){
                Newpic1.className = "pic-2";
            }
            else{
                Newpic1.className = "pic-3";
            }
            const NewImageContainer1 = document.createElement("div");
            
            if(i<3){
                NewImageContainer1.className = "image-container-1";
            }else if(i%10 ===3 || i%10 ===8 ){
                NewImageContainer1.className = "image-container-2";
            }
            else{
                NewImageContainer1.className = "image-container-3";
            }
            NewImageContainer1.style.backgroundImage = `url(${imageFirst})`;



            const NewPromotion1= document.createElement("div");
            
            if(i<3){
                NewPromotion1.className = "promotion-1";
            }else if(i%10 ===3 || i%10 ===8 ){
                NewPromotion1.className = "title-1";
            }
            else{
                NewPromotion1.className = "title-2";
            }
            const NewText = document.createElement("div");
            NewText.className = "new-text";
            NewText.textContent = title;
            
            const NewStar= document.createElement("div");
            
            block.appendChild(NewBox);
            NewBox.appendChild(Newpic1);
            Newpic1.appendChild(NewImageContainer1);
            NewImageContainer1.appendChild(NewStar);
            if(i<3){
                NewBox.appendChild(NewPromotion1);
                NewPromotion1.appendChild(NewText);
            }else{
                NewStar.className = "star";
                NewImageContainer1.appendChild(NewPromotion1);
                NewPromotion1.appendChild(NewText);
            }

            
            console.log(`${title},${imageFirst}`);
        }
    });