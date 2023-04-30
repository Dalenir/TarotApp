import React from "react";
import './Preview.css'
import {field} from "../../interfacesa";


export default function Preview({number, description, card, name}:field) {

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
                    <div className='shadow-number'>
                        {number}
                    </div>
                    <div className='description-field'>
                        <h4>{name}</h4>
                        <p>{description}</p>
                    </div>
                </div>
                <div className='text-pf'>
                    <div className='shadow-number'>
                        {card.value}
                    </div>
                    <div className='description-field'>
                        <h3>{card.name}</h3>
                        <p>{card.description}</p>
                    </div>
                </div>
            </div>
        </div>
    )
}