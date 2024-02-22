// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::OpsWorksCM::Server
 */
export class Server extends pulumi.CustomResource {
    /**
     * Get an existing Server resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Server {
        return new Server(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:opsworkscm:Server';

    /**
     * Returns true if the given object is an instance of Server.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Server {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Server.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly associatePublicIpAddress!: pulumi.Output<boolean | undefined>;
    public readonly backupId!: pulumi.Output<string | undefined>;
    public readonly backupRetentionCount!: pulumi.Output<number | undefined>;
    public readonly customCertificate!: pulumi.Output<string | undefined>;
    public readonly customDomain!: pulumi.Output<string | undefined>;
    public readonly customPrivateKey!: pulumi.Output<string | undefined>;
    public readonly disableAutomatedBackup!: pulumi.Output<boolean | undefined>;
    public /*out*/ readonly endpoint!: pulumi.Output<string>;
    public readonly engine!: pulumi.Output<string | undefined>;
    public readonly engineAttributes!: pulumi.Output<outputs.opsworkscm.ServerEngineAttribute[] | undefined>;
    public readonly engineModel!: pulumi.Output<string | undefined>;
    public readonly engineVersion!: pulumi.Output<string | undefined>;
    public readonly instanceProfileArn!: pulumi.Output<string>;
    public readonly instanceType!: pulumi.Output<string>;
    public readonly keyPair!: pulumi.Output<string | undefined>;
    public readonly preferredBackupWindow!: pulumi.Output<string | undefined>;
    public readonly preferredMaintenanceWindow!: pulumi.Output<string | undefined>;
    public readonly securityGroupIds!: pulumi.Output<string[] | undefined>;
    public readonly serverName!: pulumi.Output<string>;
    public readonly serviceRoleArn!: pulumi.Output<string>;
    public readonly subnetIds!: pulumi.Output<string[] | undefined>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a Server resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ServerArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.instanceProfileArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceProfileArn'");
            }
            if ((!args || args.instanceType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceType'");
            }
            if ((!args || args.serviceRoleArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceRoleArn'");
            }
            resourceInputs["associatePublicIpAddress"] = args ? args.associatePublicIpAddress : undefined;
            resourceInputs["backupId"] = args ? args.backupId : undefined;
            resourceInputs["backupRetentionCount"] = args ? args.backupRetentionCount : undefined;
            resourceInputs["customCertificate"] = args ? args.customCertificate : undefined;
            resourceInputs["customDomain"] = args ? args.customDomain : undefined;
            resourceInputs["customPrivateKey"] = args ? args.customPrivateKey : undefined;
            resourceInputs["disableAutomatedBackup"] = args ? args.disableAutomatedBackup : undefined;
            resourceInputs["engine"] = args ? args.engine : undefined;
            resourceInputs["engineAttributes"] = args ? args.engineAttributes : undefined;
            resourceInputs["engineModel"] = args ? args.engineModel : undefined;
            resourceInputs["engineVersion"] = args ? args.engineVersion : undefined;
            resourceInputs["instanceProfileArn"] = args ? args.instanceProfileArn : undefined;
            resourceInputs["instanceType"] = args ? args.instanceType : undefined;
            resourceInputs["keyPair"] = args ? args.keyPair : undefined;
            resourceInputs["preferredBackupWindow"] = args ? args.preferredBackupWindow : undefined;
            resourceInputs["preferredMaintenanceWindow"] = args ? args.preferredMaintenanceWindow : undefined;
            resourceInputs["securityGroupIds"] = args ? args.securityGroupIds : undefined;
            resourceInputs["serverName"] = args ? args.serverName : undefined;
            resourceInputs["serviceRoleArn"] = args ? args.serviceRoleArn : undefined;
            resourceInputs["subnetIds"] = args ? args.subnetIds : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["endpoint"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["associatePublicIpAddress"] = undefined /*out*/;
            resourceInputs["backupId"] = undefined /*out*/;
            resourceInputs["backupRetentionCount"] = undefined /*out*/;
            resourceInputs["customCertificate"] = undefined /*out*/;
            resourceInputs["customDomain"] = undefined /*out*/;
            resourceInputs["customPrivateKey"] = undefined /*out*/;
            resourceInputs["disableAutomatedBackup"] = undefined /*out*/;
            resourceInputs["endpoint"] = undefined /*out*/;
            resourceInputs["engine"] = undefined /*out*/;
            resourceInputs["engineAttributes"] = undefined /*out*/;
            resourceInputs["engineModel"] = undefined /*out*/;
            resourceInputs["engineVersion"] = undefined /*out*/;
            resourceInputs["instanceProfileArn"] = undefined /*out*/;
            resourceInputs["instanceType"] = undefined /*out*/;
            resourceInputs["keyPair"] = undefined /*out*/;
            resourceInputs["preferredBackupWindow"] = undefined /*out*/;
            resourceInputs["preferredMaintenanceWindow"] = undefined /*out*/;
            resourceInputs["securityGroupIds"] = undefined /*out*/;
            resourceInputs["serverName"] = undefined /*out*/;
            resourceInputs["serviceRoleArn"] = undefined /*out*/;
            resourceInputs["subnetIds"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["associatePublicIpAddress", "backupId", "customCertificate", "customDomain", "customPrivateKey", "engine", "engineModel", "engineVersion", "instanceProfileArn", "instanceType", "keyPair", "securityGroupIds[*]", "serverName", "serviceRoleArn", "subnetIds[*]"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Server.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Server resource.
 */
export interface ServerArgs {
    associatePublicIpAddress?: pulumi.Input<boolean>;
    backupId?: pulumi.Input<string>;
    backupRetentionCount?: pulumi.Input<number>;
    customCertificate?: pulumi.Input<string>;
    customDomain?: pulumi.Input<string>;
    customPrivateKey?: pulumi.Input<string>;
    disableAutomatedBackup?: pulumi.Input<boolean>;
    engine?: pulumi.Input<string>;
    engineAttributes?: pulumi.Input<pulumi.Input<inputs.opsworkscm.ServerEngineAttributeArgs>[]>;
    engineModel?: pulumi.Input<string>;
    engineVersion?: pulumi.Input<string>;
    instanceProfileArn: pulumi.Input<string>;
    instanceType: pulumi.Input<string>;
    keyPair?: pulumi.Input<string>;
    preferredBackupWindow?: pulumi.Input<string>;
    preferredMaintenanceWindow?: pulumi.Input<string>;
    securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    serverName?: pulumi.Input<string>;
    serviceRoleArn: pulumi.Input<string>;
    subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
