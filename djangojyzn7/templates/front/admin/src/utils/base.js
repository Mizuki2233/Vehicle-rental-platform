const base = {
    get() {
        return {
            url : "http://localhost:8080/djangojyzn7/",
            name: "djangojyzn7",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "共享用车平台"
        } 
    }
}
export default base
