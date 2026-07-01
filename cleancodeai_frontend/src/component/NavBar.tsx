import { type ChangeEvent } from "react"
const NavBar = () => {

    const onSelectModel = (e:ChangeEvent<HTMLSelectElement>) => {
        console.log(e.target.value)
    }

    return (
        <>
            <select onChange={onSelectModel}>
                <option>Gemma 4</option>
                <option>Deepseek</option>
            </select>
        </>
    )

}

export default NavBar;