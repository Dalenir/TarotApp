import React from "react";
import './Preview.css'
import {field} from "../../interfacesa";


export default function Preview({number, description, card}:field) {

    return (
        <div className='prev-container'>
            <img
                src={`${import.meta.env.VITE_API_ROOT}/card/${card.id}`}
                alt='Bah no image'
                style={{borderRadius: '10px',
                    height: "40vh",
                    width: "26vh",
                }}
            />
            <p className="reverse_text">
                {!card.state && "Reversed"}
            </p>
            <div className='prev-text'>
                <div className='text-pf'>
                    <h3>Field {number}</h3>
                    <p>{description}</p>
                </div>
                <div className='text-pf'>
                    <h3>{card.name}</h3>
                    <p>{card.description}</p>
                </div>
            </div>
        </div>
    )
}