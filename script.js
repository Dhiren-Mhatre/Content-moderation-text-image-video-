document.getElementById('uploadForm').addEventListener('submit', function(event) {
  event.preventDefault();
  
  var formData = new FormData(this);
  
  fetch('upload.php', {
    method: 'POST',
    body: formData
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    if (data && data.success) {
      if (data.image) {
        document.getElementById('imagePreview').innerHTML = `<img src="${data.image}" alt="Uploaded Image">`;
      }
      if (data.video) {
        document.getElementById('videoPreview').innerHTML = `<video controls><source src="${data.video}" type="video/mp4">Your browser does not support the video tag.</video>`;
      }
    } else {
      throw new Error('Received invalid response from server');
    }
  })
  .catch(error => {
    console.error('Error:', error);
    alert('An error occurred while processing the request. Please try again later.');
  });
});
