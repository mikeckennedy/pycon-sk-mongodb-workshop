class PackageService:
    @classmethod
    def package_count(cls):
        return 0

    @classmethod
    def release_count(cls):
        return 0

    @classmethod
    def user_count(cls):
        return 0

    @classmethod
    def download_count(cls):
        return 0

    @classmethod
    def popular_packages(cls, limit: int):
        return []

    @classmethod
    def maintainers(cls, package):
        return []

    @classmethod
    def find_package_by_name(cls, name):
        return None

    @classmethod
    def latest_package_release(cls, package):
        return None
