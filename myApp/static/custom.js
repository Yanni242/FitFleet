// BMI Tab Pop Up 
function openUnit(evt, unitName)
{
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    for(i = 0; i < tabcontent.length; i++)
    {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for(i = 0; i < tablinks.length; i++)
    {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    document.getElementById(unitName).style.display = "block";
    if (evt) 
    {
        evt.currentTarget.className += " active";
    } 
    else 
    {
        // If the function is called without an event, manually set the 'active' class on the default tab
        var defaultTab = document.querySelector(".tablinks");
        if (defaultTab) 
        {
            defaultTab.className += " active";
        }
    }
}

// Automatically open Metric units tab on page load
document.addEventListener('DOMContentLoaded', function() 
{
    openUnit(null, 'metric');
});

