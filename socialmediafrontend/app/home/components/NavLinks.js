import Link from "next/link"


const NavLinks = ({ icon, link }) => {
    return (
        <div className="flex justify-between w-full">

            <Link href={link} className="w-full h-10 flex items-center justify-center text-[22px] text-gray-100">
                {icon}
            </Link>
            <span className="h-10 w-1" />
        </div>
    )
}

export default NavLinks
