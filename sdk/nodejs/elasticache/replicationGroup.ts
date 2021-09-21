// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ElastiCache::ReplicationGroup
 *
 * @deprecated ReplicationGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class ReplicationGroup extends pulumi.CustomResource {
    /**
     * Get an existing ReplicationGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ReplicationGroup {
        pulumi.log.warn("ReplicationGroup is deprecated: ReplicationGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new ReplicationGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:elasticache:ReplicationGroup';

    /**
     * Returns true if the given object is an instance of ReplicationGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ReplicationGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ReplicationGroup.__pulumiType;
    }

    public readonly atRestEncryptionEnabled!: pulumi.Output<boolean | undefined>;
    public readonly authToken!: pulumi.Output<string | undefined>;
    public readonly autoMinorVersionUpgrade!: pulumi.Output<boolean | undefined>;
    public readonly automaticFailoverEnabled!: pulumi.Output<boolean | undefined>;
    public readonly cacheNodeType!: pulumi.Output<string | undefined>;
    public readonly cacheParameterGroupName!: pulumi.Output<string | undefined>;
    public readonly cacheSecurityGroupNames!: pulumi.Output<string[] | undefined>;
    public readonly cacheSubnetGroupName!: pulumi.Output<string | undefined>;
    public readonly configurationEndPointAddress!: pulumi.Output<string | undefined>;
    public readonly configurationEndPointPort!: pulumi.Output<string | undefined>;
    public readonly engine!: pulumi.Output<string | undefined>;
    public readonly engineVersion!: pulumi.Output<string | undefined>;
    public readonly globalReplicationGroupId!: pulumi.Output<string | undefined>;
    public readonly kmsKeyId!: pulumi.Output<string | undefined>;
    public readonly logDeliveryConfigurations!: pulumi.Output<outputs.elasticache.ReplicationGroupLogDeliveryConfigurationRequest[] | undefined>;
    public readonly multiAZEnabled!: pulumi.Output<boolean | undefined>;
    public readonly nodeGroupConfiguration!: pulumi.Output<outputs.elasticache.ReplicationGroupNodeGroupConfiguration[] | undefined>;
    public readonly notificationTopicArn!: pulumi.Output<string | undefined>;
    public readonly numCacheClusters!: pulumi.Output<number | undefined>;
    public readonly numNodeGroups!: pulumi.Output<number | undefined>;
    public readonly port!: pulumi.Output<number | undefined>;
    public readonly preferredCacheClusterAZs!: pulumi.Output<string[] | undefined>;
    public readonly preferredMaintenanceWindow!: pulumi.Output<string | undefined>;
    public readonly primaryClusterId!: pulumi.Output<string | undefined>;
    public readonly primaryEndPointAddress!: pulumi.Output<string | undefined>;
    public readonly primaryEndPointPort!: pulumi.Output<string | undefined>;
    public readonly readEndPointAddresses!: pulumi.Output<string | undefined>;
    public readonly readEndPointAddressesList!: pulumi.Output<string[] | undefined>;
    public readonly readEndPointPorts!: pulumi.Output<string | undefined>;
    public readonly readEndPointPortsList!: pulumi.Output<string[] | undefined>;
    public readonly readerEndPointAddress!: pulumi.Output<string | undefined>;
    public readonly readerEndPointPort!: pulumi.Output<string | undefined>;
    public readonly replicasPerNodeGroup!: pulumi.Output<number | undefined>;
    public readonly replicationGroupDescription!: pulumi.Output<string>;
    public /*out*/ readonly replicationGroupId!: pulumi.Output<string>;
    public readonly securityGroupIds!: pulumi.Output<string[] | undefined>;
    public readonly snapshotArns!: pulumi.Output<string[] | undefined>;
    public readonly snapshotName!: pulumi.Output<string | undefined>;
    public readonly snapshotRetentionLimit!: pulumi.Output<number | undefined>;
    public readonly snapshotWindow!: pulumi.Output<string | undefined>;
    public readonly snapshottingClusterId!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.elasticache.ReplicationGroupTag[] | undefined>;
    public readonly transitEncryptionEnabled!: pulumi.Output<boolean | undefined>;
    public readonly userGroupIds!: pulumi.Output<string[] | undefined>;

    /**
     * Create a ReplicationGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated ReplicationGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ReplicationGroupArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("ReplicationGroup is deprecated: ReplicationGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.replicationGroupDescription === undefined) && !opts.urn) {
                throw new Error("Missing required property 'replicationGroupDescription'");
            }
            inputs["atRestEncryptionEnabled"] = args ? args.atRestEncryptionEnabled : undefined;
            inputs["authToken"] = args ? args.authToken : undefined;
            inputs["autoMinorVersionUpgrade"] = args ? args.autoMinorVersionUpgrade : undefined;
            inputs["automaticFailoverEnabled"] = args ? args.automaticFailoverEnabled : undefined;
            inputs["cacheNodeType"] = args ? args.cacheNodeType : undefined;
            inputs["cacheParameterGroupName"] = args ? args.cacheParameterGroupName : undefined;
            inputs["cacheSecurityGroupNames"] = args ? args.cacheSecurityGroupNames : undefined;
            inputs["cacheSubnetGroupName"] = args ? args.cacheSubnetGroupName : undefined;
            inputs["configurationEndPointAddress"] = args ? args.configurationEndPointAddress : undefined;
            inputs["configurationEndPointPort"] = args ? args.configurationEndPointPort : undefined;
            inputs["engine"] = args ? args.engine : undefined;
            inputs["engineVersion"] = args ? args.engineVersion : undefined;
            inputs["globalReplicationGroupId"] = args ? args.globalReplicationGroupId : undefined;
            inputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            inputs["logDeliveryConfigurations"] = args ? args.logDeliveryConfigurations : undefined;
            inputs["multiAZEnabled"] = args ? args.multiAZEnabled : undefined;
            inputs["nodeGroupConfiguration"] = args ? args.nodeGroupConfiguration : undefined;
            inputs["notificationTopicArn"] = args ? args.notificationTopicArn : undefined;
            inputs["numCacheClusters"] = args ? args.numCacheClusters : undefined;
            inputs["numNodeGroups"] = args ? args.numNodeGroups : undefined;
            inputs["port"] = args ? args.port : undefined;
            inputs["preferredCacheClusterAZs"] = args ? args.preferredCacheClusterAZs : undefined;
            inputs["preferredMaintenanceWindow"] = args ? args.preferredMaintenanceWindow : undefined;
            inputs["primaryClusterId"] = args ? args.primaryClusterId : undefined;
            inputs["primaryEndPointAddress"] = args ? args.primaryEndPointAddress : undefined;
            inputs["primaryEndPointPort"] = args ? args.primaryEndPointPort : undefined;
            inputs["readEndPointAddresses"] = args ? args.readEndPointAddresses : undefined;
            inputs["readEndPointAddressesList"] = args ? args.readEndPointAddressesList : undefined;
            inputs["readEndPointPorts"] = args ? args.readEndPointPorts : undefined;
            inputs["readEndPointPortsList"] = args ? args.readEndPointPortsList : undefined;
            inputs["readerEndPointAddress"] = args ? args.readerEndPointAddress : undefined;
            inputs["readerEndPointPort"] = args ? args.readerEndPointPort : undefined;
            inputs["replicasPerNodeGroup"] = args ? args.replicasPerNodeGroup : undefined;
            inputs["replicationGroupDescription"] = args ? args.replicationGroupDescription : undefined;
            inputs["securityGroupIds"] = args ? args.securityGroupIds : undefined;
            inputs["snapshotArns"] = args ? args.snapshotArns : undefined;
            inputs["snapshotName"] = args ? args.snapshotName : undefined;
            inputs["snapshotRetentionLimit"] = args ? args.snapshotRetentionLimit : undefined;
            inputs["snapshotWindow"] = args ? args.snapshotWindow : undefined;
            inputs["snapshottingClusterId"] = args ? args.snapshottingClusterId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["transitEncryptionEnabled"] = args ? args.transitEncryptionEnabled : undefined;
            inputs["userGroupIds"] = args ? args.userGroupIds : undefined;
            inputs["replicationGroupId"] = undefined /*out*/;
        } else {
            inputs["atRestEncryptionEnabled"] = undefined /*out*/;
            inputs["authToken"] = undefined /*out*/;
            inputs["autoMinorVersionUpgrade"] = undefined /*out*/;
            inputs["automaticFailoverEnabled"] = undefined /*out*/;
            inputs["cacheNodeType"] = undefined /*out*/;
            inputs["cacheParameterGroupName"] = undefined /*out*/;
            inputs["cacheSecurityGroupNames"] = undefined /*out*/;
            inputs["cacheSubnetGroupName"] = undefined /*out*/;
            inputs["configurationEndPointAddress"] = undefined /*out*/;
            inputs["configurationEndPointPort"] = undefined /*out*/;
            inputs["engine"] = undefined /*out*/;
            inputs["engineVersion"] = undefined /*out*/;
            inputs["globalReplicationGroupId"] = undefined /*out*/;
            inputs["kmsKeyId"] = undefined /*out*/;
            inputs["logDeliveryConfigurations"] = undefined /*out*/;
            inputs["multiAZEnabled"] = undefined /*out*/;
            inputs["nodeGroupConfiguration"] = undefined /*out*/;
            inputs["notificationTopicArn"] = undefined /*out*/;
            inputs["numCacheClusters"] = undefined /*out*/;
            inputs["numNodeGroups"] = undefined /*out*/;
            inputs["port"] = undefined /*out*/;
            inputs["preferredCacheClusterAZs"] = undefined /*out*/;
            inputs["preferredMaintenanceWindow"] = undefined /*out*/;
            inputs["primaryClusterId"] = undefined /*out*/;
            inputs["primaryEndPointAddress"] = undefined /*out*/;
            inputs["primaryEndPointPort"] = undefined /*out*/;
            inputs["readEndPointAddresses"] = undefined /*out*/;
            inputs["readEndPointAddressesList"] = undefined /*out*/;
            inputs["readEndPointPorts"] = undefined /*out*/;
            inputs["readEndPointPortsList"] = undefined /*out*/;
            inputs["readerEndPointAddress"] = undefined /*out*/;
            inputs["readerEndPointPort"] = undefined /*out*/;
            inputs["replicasPerNodeGroup"] = undefined /*out*/;
            inputs["replicationGroupDescription"] = undefined /*out*/;
            inputs["replicationGroupId"] = undefined /*out*/;
            inputs["securityGroupIds"] = undefined /*out*/;
            inputs["snapshotArns"] = undefined /*out*/;
            inputs["snapshotName"] = undefined /*out*/;
            inputs["snapshotRetentionLimit"] = undefined /*out*/;
            inputs["snapshotWindow"] = undefined /*out*/;
            inputs["snapshottingClusterId"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["transitEncryptionEnabled"] = undefined /*out*/;
            inputs["userGroupIds"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ReplicationGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ReplicationGroup resource.
 */
export interface ReplicationGroupArgs {
    atRestEncryptionEnabled?: pulumi.Input<boolean>;
    authToken?: pulumi.Input<string>;
    autoMinorVersionUpgrade?: pulumi.Input<boolean>;
    automaticFailoverEnabled?: pulumi.Input<boolean>;
    cacheNodeType?: pulumi.Input<string>;
    cacheParameterGroupName?: pulumi.Input<string>;
    cacheSecurityGroupNames?: pulumi.Input<pulumi.Input<string>[]>;
    cacheSubnetGroupName?: pulumi.Input<string>;
    configurationEndPointAddress?: pulumi.Input<string>;
    configurationEndPointPort?: pulumi.Input<string>;
    engine?: pulumi.Input<string>;
    engineVersion?: pulumi.Input<string>;
    globalReplicationGroupId?: pulumi.Input<string>;
    kmsKeyId?: pulumi.Input<string>;
    logDeliveryConfigurations?: pulumi.Input<pulumi.Input<inputs.elasticache.ReplicationGroupLogDeliveryConfigurationRequestArgs>[]>;
    multiAZEnabled?: pulumi.Input<boolean>;
    nodeGroupConfiguration?: pulumi.Input<pulumi.Input<inputs.elasticache.ReplicationGroupNodeGroupConfigurationArgs>[]>;
    notificationTopicArn?: pulumi.Input<string>;
    numCacheClusters?: pulumi.Input<number>;
    numNodeGroups?: pulumi.Input<number>;
    port?: pulumi.Input<number>;
    preferredCacheClusterAZs?: pulumi.Input<pulumi.Input<string>[]>;
    preferredMaintenanceWindow?: pulumi.Input<string>;
    primaryClusterId?: pulumi.Input<string>;
    primaryEndPointAddress?: pulumi.Input<string>;
    primaryEndPointPort?: pulumi.Input<string>;
    readEndPointAddresses?: pulumi.Input<string>;
    readEndPointAddressesList?: pulumi.Input<pulumi.Input<string>[]>;
    readEndPointPorts?: pulumi.Input<string>;
    readEndPointPortsList?: pulumi.Input<pulumi.Input<string>[]>;
    readerEndPointAddress?: pulumi.Input<string>;
    readerEndPointPort?: pulumi.Input<string>;
    replicasPerNodeGroup?: pulumi.Input<number>;
    replicationGroupDescription: pulumi.Input<string>;
    securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    snapshotArns?: pulumi.Input<pulumi.Input<string>[]>;
    snapshotName?: pulumi.Input<string>;
    snapshotRetentionLimit?: pulumi.Input<number>;
    snapshotWindow?: pulumi.Input<string>;
    snapshottingClusterId?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.elasticache.ReplicationGroupTagArgs>[]>;
    transitEncryptionEnabled?: pulumi.Input<boolean>;
    userGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
}
