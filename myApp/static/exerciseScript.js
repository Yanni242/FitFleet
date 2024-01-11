// Dropdown function 
function toggleDropdown(id, event) 
{
    // Prevent dropdown from closing when not pressed
    if (event) 
    {
        event.stopPropagation();
    }
    
    // Toggle the display of the clicked dropdown
    var dropdown = document.getElementById(id);
    var isHidden = dropdown.style.display === 'none' || !dropdown.style.display;

    dropdown.style.display = isHidden ? 'block' : 'none';

    if (isHidden) 
    {
        // If the dropdown was hidden and is now shown, scroll it into view
        setTimeout(function() 
        {
            dropdown.scrollIntoView({ behavior: 'smooth', block: 'end' });
        }, 0);
    }
}


// Exercise Info Tab Pop up 
function openExerciseModal(name, description, tips, video_url) 
{
    document.getElementById("exerciseName").innerText = name;
    document.getElementById("exerciseDescription").innerText = description;
    document.getElementById("exerciseTips").innerText = tips;
    document.getElementById('exerciseVideoIframe').src = video_url;
    document.getElementById("exerciseModal").style.display = "block";
}

function closeModal() 
{
    document.getElementById("exerciseModal").style.display = "none";
    document.getElementById('exerciseVideoIframe').src = '';
}

document.querySelectorAll('.exercise-button').forEach(button => {
    button.addEventListener('click', (event) => {
        event.stopPropagation();
    });
});