import './App.css';
import VerticalCard from './Components/VerticalCard';
import TextField from '@mui/material/TextField';
import { useEffect, useState } from 'react';

const url = "http://localhost:5000/"

const fetchResource = async (url, method) => {
  const headers = {
    /* add headers here */
  }

  try {
    const resp = await fetch(url, { method: method, headers: headers });

    /* Deal with headers here. If we decide to deal with them externally, rethink design */
    
    const type = resp.headers.get("Content-Type");
    if (type.includes("text/html")) {
      return await resp.text();
    } if (type.includes("application/json")) {
      return await resp.json();
    }
  } catch (error) {
    console.error("Error fetching resource: ", error);
  }
}

function App() {

  const [searchInput, setSearchInput] = useState('');

  useEffect(() => {
    fetchResource(url + "students", "GET").then(data => console.log(data));
    fetchResource(url, "GET").then(data => console.log(data));
  }, []);

  const handleInputChange = (event) => {
    setSearchInput(event.target.value);
  };

  const person = {
    "firstName": "Tyler",
    "lastName": "Cushing",
    "lab": "AYC",
    "date": "9:53AM 9/10/22",
    "notes": "No notes"
  };

  let people = [person]

  let people_new = people.filter((el) => {
		if (searchInput === '') {
			return el;
		} else {
      var values = [];
      for (var key in el) {
        values.push(el[key]);
      }
      return values.includes(searchInput);
		}
	})

  return (
    <div className='student_row'>
      <TextField id="outlined-basic" value={searchInput} onChange={handleInputChange} label="Search for a student..." variant="outlined" />
      {people_new.map((item, index) => (
          <VerticalCard key={index} name={item["firstName"] + " " + item["lastName"]} lab={item["lab"]} date={item["date"]} notes={item["notes"]} />
        ))}
    </div>
  );
}

export default App;

// import './App.css';
// import * as React from 'react';
// import ActionAreaCard from '../src/Components/ActionAreaCard';
// import TextField from '@mui/material/TextField';
// import MultipleSelectCheckmarks from '../src/Components/Tags';
// import { useState } from 'react';
// import { useEffect } from 'react';

// import { data } from './clubs';

// import { usePapaParse } from 'react-papaparse';
// import BasicSelect from './Components/Accordian';


// function App() {
//   const [nameUserInput, setNameUserInput] = useState('');
//   const [descriptionUserInput, setDescriptionUserInput] = useState('');
  
//   const handleNameInputChange = (event) => {
//     setNameUserInput(event.target.value);
//   };

//   const handleDescriptionInputChange = (event) => {
//     setDescriptionUserInput(event.target.value);
//   };


//   let [card_info, updateCardInfo] = useState([]);

  
//   const { readString } = usePapaParse();
//   useEffect(() => {
//     let card_info = [];
//     const csvString = data;
    
//     readString(csvString, {
//       worker: true,
//       complete: (results) => {
//         results.data.forEach((cardData) => {
//           const innerArray = cardData.slice(2); // Create the inner array starting from index 2
//           card_info.push([cardData[0], cardData[1], innerArray]);
//           updateCardInfo([...card_info, [cardData[0], cardData[1], innerArray]]);
//         });
//       },
//     });

//   });

//   let textArray = card_info;

//   let text_array_new = textArray.filter((el) => {
// 		if (nameUserInput === '') {
// 			return el;
// 		} else {
// 			var to_check = el.at(0).toLowerCase();
// 			return to_check.includes(nameUserInput);
// 		}
// 	})

//   let descriptions_array = textArray.filter((el) => {
// 		if (descriptionUserInput === '') {
// 			return el;
// 		} else {
// 			var to_check = el.at(1).toLowerCase();
// 			return to_check.includes(descriptionUserInput);
// 		}
// 	})

//   const [personName, setPersonName] = React.useState([]);

//   let tags_array = [];

//   tags_array = card_info.filter((el) => {
//     if (personName.length === 0) {
//       return el;
//     } else {
//       return personName.some((tag) => el.at(2).includes(tag));
//     }
//   });

//   const [age, setAge] = useState('');


//   const handleChangeTags = (event) => {
//     const {
//       target: { value },
//     } = event;
//     setPersonName(
//       // On autofill we get a stringified value.
//       typeof value === 'string' ? value.split(',') : value,
//     );
//     console.log(personName);
//   };

//   const handleChange = (event) => {
//     setAge(event.target.value);
//     console.log(age)
//   };


//   return (
//     <div className="container mx-auto bg-gray-200 rounded-xl shadow border p-8 m-10" id='clubs_holder'>
//       <p className="text-3xl text-gray-700 font-bold mb-5">
//         Welcome!
//       </p>

//       <BasicSelect age={age} handleChange={handleChange} />

      

//       {age === 10 && <TextField label="Type in a name.." value={nameUserInput} onChange={handleNameInputChange} sx={{paddingBottom: '10px'}} />}
//       {age === 20 && <TextField label="Type key words..." value={descriptionUserInput} onChange={handleDescriptionInputChange} sx={{paddingBottom: '10px'}} />}
//       {age === 30 && <MultipleSelectCheckmarks personName={personName} handleChange={handleChangeTags} />}

//       <div className='card-container'>

//       {age === 10 &&
//         text_array_new.map((item, index) => (
//           <ActionAreaCard key={index} title={item.at(0)} description={item.at(1)} tags={item.at(2)} />
//         ))}

//       {age === 20 &&
//         descriptions_array.map((item, index) => (
//           <ActionAreaCard key={index} title={item.at(0)} description={item.at(1)} tags={item.at(2)} />
//         ))}

//       {age === 30 &&
//               tags_array.map((item, index) => (
//                 <ActionAreaCard key={index} title={item.at(0)} description={item.at(1)} tags={item.at(2)} />
//               ))}
//       </div>

      

//     </div>
//   );
// }

// export default App;
