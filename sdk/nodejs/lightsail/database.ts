// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Lightsail::Database
 */
export class Database extends pulumi.CustomResource {
    /**
     * Get an existing Database resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Database {
        return new Database(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:lightsail:Database';

    /**
     * Returns true if the given object is an instance of Database.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Database {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Database.__pulumiType;
    }

    /**
     * The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format.
     */
    public readonly availabilityZone!: pulumi.Output<string | undefined>;
    /**
     * When true, enables automated backup retention for your database. Updates are applied during the next maintenance window because this can result in an outage.
     */
    public readonly backupRetention!: pulumi.Output<boolean | undefined>;
    /**
     * Indicates the certificate that needs to be associated with the database.
     */
    public readonly caCertificateIdentifier!: pulumi.Output<string | undefined>;
    public /*out*/ readonly databaseArn!: pulumi.Output<string>;
    /**
     * The name of the database to create when the Lightsail database resource is created. For MySQL, if this parameter isn't specified, no database is created in the database resource. For PostgreSQL, if this parameter isn't specified, a database named postgres is created in the database resource.
     */
    public readonly masterDatabaseName!: pulumi.Output<string>;
    /**
     * The password for the master user. The password can include any printable ASCII character except "/", """, or "@". It cannot contain spaces.
     */
    public readonly masterUserPassword!: pulumi.Output<string | undefined>;
    /**
     * The name for the master user.
     */
    public readonly masterUsername!: pulumi.Output<string>;
    /**
     * The daily time range during which automated backups are created for your new database if automated backups are enabled.
     */
    public readonly preferredBackupWindow!: pulumi.Output<string | undefined>;
    /**
     * The weekly time range during which system maintenance can occur on your new database.
     */
    public readonly preferredMaintenanceWindow!: pulumi.Output<string | undefined>;
    /**
     * Specifies the accessibility options for your new database. A value of true specifies a database that is available to resources outside of your Lightsail account. A value of false specifies a database that is available only to your Lightsail resources in the same region as your database.
     */
    public readonly publiclyAccessible!: pulumi.Output<boolean | undefined>;
    /**
     * The blueprint ID for your new database. A blueprint describes the major engine version of a database.
     */
    public readonly relationalDatabaseBlueprintId!: pulumi.Output<string>;
    /**
     * The bundle ID for your new database. A bundle describes the performance specifications for your database.
     */
    public readonly relationalDatabaseBundleId!: pulumi.Output<string>;
    /**
     * The name to use for your new Lightsail database resource.
     */
    public readonly relationalDatabaseName!: pulumi.Output<string>;
    /**
     * Update one or more parameters of the relational database.
     */
    public readonly relationalDatabaseParameters!: pulumi.Output<outputs.lightsail.DatabaseRelationalDatabaseParameter[] | undefined>;
    /**
     * When true, the master user password is changed to a new strong password generated by Lightsail. Use the get relational database master user password operation to get the new password.
     */
    public readonly rotateMasterUserPassword!: pulumi.Output<boolean | undefined>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a Database resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DatabaseArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.masterDatabaseName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'masterDatabaseName'");
            }
            if ((!args || args.masterUsername === undefined) && !opts.urn) {
                throw new Error("Missing required property 'masterUsername'");
            }
            if ((!args || args.relationalDatabaseBlueprintId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'relationalDatabaseBlueprintId'");
            }
            if ((!args || args.relationalDatabaseBundleId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'relationalDatabaseBundleId'");
            }
            if ((!args || args.relationalDatabaseName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'relationalDatabaseName'");
            }
            resourceInputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            resourceInputs["backupRetention"] = args ? args.backupRetention : undefined;
            resourceInputs["caCertificateIdentifier"] = args ? args.caCertificateIdentifier : undefined;
            resourceInputs["masterDatabaseName"] = args ? args.masterDatabaseName : undefined;
            resourceInputs["masterUserPassword"] = args ? args.masterUserPassword : undefined;
            resourceInputs["masterUsername"] = args ? args.masterUsername : undefined;
            resourceInputs["preferredBackupWindow"] = args ? args.preferredBackupWindow : undefined;
            resourceInputs["preferredMaintenanceWindow"] = args ? args.preferredMaintenanceWindow : undefined;
            resourceInputs["publiclyAccessible"] = args ? args.publiclyAccessible : undefined;
            resourceInputs["relationalDatabaseBlueprintId"] = args ? args.relationalDatabaseBlueprintId : undefined;
            resourceInputs["relationalDatabaseBundleId"] = args ? args.relationalDatabaseBundleId : undefined;
            resourceInputs["relationalDatabaseName"] = args ? args.relationalDatabaseName : undefined;
            resourceInputs["relationalDatabaseParameters"] = args ? args.relationalDatabaseParameters : undefined;
            resourceInputs["rotateMasterUserPassword"] = args ? args.rotateMasterUserPassword : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["databaseArn"] = undefined /*out*/;
        } else {
            resourceInputs["availabilityZone"] = undefined /*out*/;
            resourceInputs["backupRetention"] = undefined /*out*/;
            resourceInputs["caCertificateIdentifier"] = undefined /*out*/;
            resourceInputs["databaseArn"] = undefined /*out*/;
            resourceInputs["masterDatabaseName"] = undefined /*out*/;
            resourceInputs["masterUserPassword"] = undefined /*out*/;
            resourceInputs["masterUsername"] = undefined /*out*/;
            resourceInputs["preferredBackupWindow"] = undefined /*out*/;
            resourceInputs["preferredMaintenanceWindow"] = undefined /*out*/;
            resourceInputs["publiclyAccessible"] = undefined /*out*/;
            resourceInputs["relationalDatabaseBlueprintId"] = undefined /*out*/;
            resourceInputs["relationalDatabaseBundleId"] = undefined /*out*/;
            resourceInputs["relationalDatabaseName"] = undefined /*out*/;
            resourceInputs["relationalDatabaseParameters"] = undefined /*out*/;
            resourceInputs["rotateMasterUserPassword"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["availabilityZone", "masterDatabaseName", "masterUsername", "relationalDatabaseBlueprintId", "relationalDatabaseBundleId", "relationalDatabaseName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Database.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Database resource.
 */
export interface DatabaseArgs {
    /**
     * The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format.
     */
    availabilityZone?: pulumi.Input<string>;
    /**
     * When true, enables automated backup retention for your database. Updates are applied during the next maintenance window because this can result in an outage.
     */
    backupRetention?: pulumi.Input<boolean>;
    /**
     * Indicates the certificate that needs to be associated with the database.
     */
    caCertificateIdentifier?: pulumi.Input<string>;
    /**
     * The name of the database to create when the Lightsail database resource is created. For MySQL, if this parameter isn't specified, no database is created in the database resource. For PostgreSQL, if this parameter isn't specified, a database named postgres is created in the database resource.
     */
    masterDatabaseName: pulumi.Input<string>;
    /**
     * The password for the master user. The password can include any printable ASCII character except "/", """, or "@". It cannot contain spaces.
     */
    masterUserPassword?: pulumi.Input<string>;
    /**
     * The name for the master user.
     */
    masterUsername: pulumi.Input<string>;
    /**
     * The daily time range during which automated backups are created for your new database if automated backups are enabled.
     */
    preferredBackupWindow?: pulumi.Input<string>;
    /**
     * The weekly time range during which system maintenance can occur on your new database.
     */
    preferredMaintenanceWindow?: pulumi.Input<string>;
    /**
     * Specifies the accessibility options for your new database. A value of true specifies a database that is available to resources outside of your Lightsail account. A value of false specifies a database that is available only to your Lightsail resources in the same region as your database.
     */
    publiclyAccessible?: pulumi.Input<boolean>;
    /**
     * The blueprint ID for your new database. A blueprint describes the major engine version of a database.
     */
    relationalDatabaseBlueprintId: pulumi.Input<string>;
    /**
     * The bundle ID for your new database. A bundle describes the performance specifications for your database.
     */
    relationalDatabaseBundleId: pulumi.Input<string>;
    /**
     * The name to use for your new Lightsail database resource.
     */
    relationalDatabaseName: pulumi.Input<string>;
    /**
     * Update one or more parameters of the relational database.
     */
    relationalDatabaseParameters?: pulumi.Input<pulumi.Input<inputs.lightsail.DatabaseRelationalDatabaseParameterArgs>[]>;
    /**
     * When true, the master user password is changed to a new strong password generated by Lightsail. Use the get relational database master user password operation to get the new password.
     */
    rotateMasterUserPassword?: pulumi.Input<boolean>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
