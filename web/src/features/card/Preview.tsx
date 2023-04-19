import React from "react";
import Field from "./Field";
import './Preview.css'
import {card, field} from "../../interfacesa";


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
            <div className='prev-text'>
                <div className='text-pf'><p>{number}: \n {card.description}</p></div>
                <div className='text-pf'><p>{description}</p></div>
            </div>
        </div>
    )
}