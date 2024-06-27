function GetMap() {
            var api_data_ip = document.getElementById('api_data_ip').innerHTML
            var api_data_loc = document.getElementById('api_data_loc').innerHTML.split(',')
            var city = document.getElementById('city').innerHTML
            var api_data_country = document.getElementById('api_data_country').innerHTML

            var map = new Microsoft.Maps.Map('#map', {
                credentials: 'YOUR_BING_MAPS_KEY',
                center: new Microsoft.Maps.Location(parseInt(api_data_loc[0],10), parseInt(api_data_loc[1],10)),
                zoom: 8
            });

            var center = map.getCenter();
            var pin = new Microsoft.Maps.Pushpin(center, {
                title: 'Center Pin',
                subTitle: city, api_data_country
            });
            map.entities.push(pin);
        }

window.onload = GetMap;