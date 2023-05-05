import {loadConfigFromFile} from "vite";

// TODO: I need something more clever with enums and styles. Backend too.

export enum Suit {
    Swords='swords',
    Cups='cups',
    Wands='wands',
    Pentacles='pentacles',
    MajorArcana='major arcana'
}

export const SuitStyle = {
    swords: {
        main_color: '#FF0000',
        secondary_color: 'rgba(255,0,0,0.65)'
    },
    cups: {
        main_color: '#6495ED',
        secondary_color: 'rgba(0,0,255,0.37)'
    },
    wands: {
        main_color: '#CD853F',
        secondary_color: 'rgba(204,84,0,0.52)'
    },
    pentacles: {
        main_color: '#FFD700',
        secondary_color: 'rgba(176,162,2,0.65)'
    },
    'major arcana': {
        main_color: '#C0C0C0',
        secondary_color: '#F0FFFF'
    }
}
