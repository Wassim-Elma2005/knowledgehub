param adminUser string = 'dblogin1'
@secure()
param adminPassword string

resource mysql 'Microsoft.DBforMySQL/flexibleServers@2023-12-30' = {
  name: 'wassimdbtest'
  location: 'spaincentral'

  sku: {
    name: 'Standard_B1ms' // goedkoopste tier
    tier: 'Burstable'
  }

  properties: {
    administratorLogin: adminUser
    administratorLoginPassword: adminPassword

    version: '8.0.21' // Wijzig de versie naar een ondersteunde versie
    storage: {
      storageSizeGB: 20
      autoGrow: 'Disabled'
    }

    network: {
      publicNetworkAccess: 'Enabled'
    }

    backup: {
      backupRetentionDays: 1
      geoRedundantBackup: 'Disabled'
    }

    highAvailability: {
      mode: 'Disabled'
    }

    maintenanceWindow: {
      customWindow: 'Disabled'
    }
  }
}