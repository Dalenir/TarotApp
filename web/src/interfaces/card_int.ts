export interface card {
    id: number,
    value: number,
    visual_value: string,
    name: string,
    suit: suit,
    state: boolean,
    stats: stats,
    description: string,
    size: { width: string, height: string }
}

export interface stats {
    good: number
    luck: number
    order: number
    wild: boolean
}

export interface suit {
    name: string
    description: string
}