"use client"
import { AiOutlinePlus } from "react-icons/ai"
// SiAzuredataexplorer

const CreatePost = () => {

    const togglePostCreateModal = () => {
        console.log("modal clicked")
    }


    return (
        <button onClick={togglePostCreateModal} className='w-8 cursor-pointer h-8 rounded-full flex justify-center items-center bg-gray-100/[0.5]'>
            <AiOutlinePlus className="text-xl text-white" />
        </button>
    )
}

export default CreatePost
