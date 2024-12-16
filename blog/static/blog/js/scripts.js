
function openModal(postId) {
   
    document.getElementById("deleteModal").style.display = "block";

   
    const form = document.getElementById("deleteForm");
    form.action = `/post/${postId}/delete/`; 
}

function closeModal() {
    
    document.getElementById("deleteModal").style.display = "none";
}

window.onclick = function(event) {
    const modal = document.getElementById("deleteModal");
    if (event.target == modal) {
        closeModal();
    }
}

