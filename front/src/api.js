const BASE_URL = "http://localhost:8000/chat"

const getRecommendation = (params) => {
    let query = `${BASE_URL}?`
        + `series_or_movie=${params.series_or_movie}&`
        + `genre=${params.genre}&`
        + `decade=${params.decade}&`
        + `age_rating=${params.age_rating}&`
        + `positive_reference=${params.positive_reference}&`
        + `negative_reference=${params.negative_reference}`
    query = query.replaceAll(' ', '%20')

    return fetch(query, { method: "POST" }).then(res => res.json())
}

export default {
    getRecommendation
}