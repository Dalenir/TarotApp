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
        secondary_color: '#c02020'
    },
    cups: {
        main_color: '#6495ED',
        secondary_color: '#8e8ed9'
    },
    wands: {
        main_color: '#CD853F',
        secondary_color: '#88522f'
    },
    pentacles: {
        main_color: '#FFD700',
        secondary_color: '#b0a202'
    },
    'major arcana': {
        main_color: '#C0C0C0',
        secondary_color: '#F0FFFF'
    }
}
