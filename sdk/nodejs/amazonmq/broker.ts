// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AmazonMQ::Broker
 *
 * @deprecated Broker is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Broker extends pulumi.CustomResource {
    /**
     * Get an existing Broker resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Broker {
        pulumi.log.warn("Broker is deprecated: Broker is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Broker(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:amazonmq:Broker';

    /**
     * Returns true if the given object is an instance of Broker.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Broker {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Broker.__pulumiType;
    }

    public /*out*/ readonly amqpEndpoints!: pulumi.Output<string[]>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly authenticationStrategy!: pulumi.Output<string | undefined>;
    public readonly autoMinorVersionUpgrade!: pulumi.Output<boolean>;
    public readonly brokerName!: pulumi.Output<string>;
    public readonly configuration!: pulumi.Output<outputs.amazonmq.BrokerConfigurationId | undefined>;
    public /*out*/ readonly configurationId!: pulumi.Output<string>;
    public /*out*/ readonly configurationRevision!: pulumi.Output<number>;
    public readonly deploymentMode!: pulumi.Output<string>;
    public readonly encryptionOptions!: pulumi.Output<outputs.amazonmq.BrokerEncryptionOptions | undefined>;
    public readonly engineType!: pulumi.Output<string>;
    public readonly engineVersion!: pulumi.Output<string>;
    public readonly hostInstanceType!: pulumi.Output<string>;
    public /*out*/ readonly ipAddresses!: pulumi.Output<string[]>;
    public readonly ldapServerMetadata!: pulumi.Output<outputs.amazonmq.BrokerLdapServerMetadata | undefined>;
    public readonly logs!: pulumi.Output<outputs.amazonmq.BrokerLogList | undefined>;
    public readonly maintenanceWindowStartTime!: pulumi.Output<outputs.amazonmq.BrokerMaintenanceWindow | undefined>;
    public /*out*/ readonly mqttEndpoints!: pulumi.Output<string[]>;
    public /*out*/ readonly openWireEndpoints!: pulumi.Output<string[]>;
    public readonly publiclyAccessible!: pulumi.Output<boolean>;
    public readonly securityGroups!: pulumi.Output<string[] | undefined>;
    public /*out*/ readonly stompEndpoints!: pulumi.Output<string[]>;
    public readonly storageType!: pulumi.Output<string | undefined>;
    public readonly subnetIds!: pulumi.Output<string[] | undefined>;
    public readonly tags!: pulumi.Output<outputs.amazonmq.BrokerTagsEntry[] | undefined>;
    public readonly users!: pulumi.Output<outputs.amazonmq.BrokerUser[]>;
    public /*out*/ readonly wssEndpoints!: pulumi.Output<string[]>;

    /**
     * Create a Broker resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Broker is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: BrokerArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Broker is deprecated: Broker is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.autoMinorVersionUpgrade === undefined) && !opts.urn) {
                throw new Error("Missing required property 'autoMinorVersionUpgrade'");
            }
            if ((!args || args.brokerName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'brokerName'");
            }
            if ((!args || args.deploymentMode === undefined) && !opts.urn) {
                throw new Error("Missing required property 'deploymentMode'");
            }
            if ((!args || args.engineType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'engineType'");
            }
            if ((!args || args.engineVersion === undefined) && !opts.urn) {
                throw new Error("Missing required property 'engineVersion'");
            }
            if ((!args || args.hostInstanceType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'hostInstanceType'");
            }
            if ((!args || args.publiclyAccessible === undefined) && !opts.urn) {
                throw new Error("Missing required property 'publiclyAccessible'");
            }
            if ((!args || args.users === undefined) && !opts.urn) {
                throw new Error("Missing required property 'users'");
            }
            inputs["authenticationStrategy"] = args ? args.authenticationStrategy : undefined;
            inputs["autoMinorVersionUpgrade"] = args ? args.autoMinorVersionUpgrade : undefined;
            inputs["brokerName"] = args ? args.brokerName : undefined;
            inputs["configuration"] = args ? args.configuration : undefined;
            inputs["deploymentMode"] = args ? args.deploymentMode : undefined;
            inputs["encryptionOptions"] = args ? args.encryptionOptions : undefined;
            inputs["engineType"] = args ? args.engineType : undefined;
            inputs["engineVersion"] = args ? args.engineVersion : undefined;
            inputs["hostInstanceType"] = args ? args.hostInstanceType : undefined;
            inputs["ldapServerMetadata"] = args ? args.ldapServerMetadata : undefined;
            inputs["logs"] = args ? args.logs : undefined;
            inputs["maintenanceWindowStartTime"] = args ? args.maintenanceWindowStartTime : undefined;
            inputs["publiclyAccessible"] = args ? args.publiclyAccessible : undefined;
            inputs["securityGroups"] = args ? args.securityGroups : undefined;
            inputs["storageType"] = args ? args.storageType : undefined;
            inputs["subnetIds"] = args ? args.subnetIds : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["users"] = args ? args.users : undefined;
            inputs["amqpEndpoints"] = undefined /*out*/;
            inputs["arn"] = undefined /*out*/;
            inputs["configurationId"] = undefined /*out*/;
            inputs["configurationRevision"] = undefined /*out*/;
            inputs["ipAddresses"] = undefined /*out*/;
            inputs["mqttEndpoints"] = undefined /*out*/;
            inputs["openWireEndpoints"] = undefined /*out*/;
            inputs["stompEndpoints"] = undefined /*out*/;
            inputs["wssEndpoints"] = undefined /*out*/;
        } else {
            inputs["amqpEndpoints"] = undefined /*out*/;
            inputs["arn"] = undefined /*out*/;
            inputs["authenticationStrategy"] = undefined /*out*/;
            inputs["autoMinorVersionUpgrade"] = undefined /*out*/;
            inputs["brokerName"] = undefined /*out*/;
            inputs["configuration"] = undefined /*out*/;
            inputs["configurationId"] = undefined /*out*/;
            inputs["configurationRevision"] = undefined /*out*/;
            inputs["deploymentMode"] = undefined /*out*/;
            inputs["encryptionOptions"] = undefined /*out*/;
            inputs["engineType"] = undefined /*out*/;
            inputs["engineVersion"] = undefined /*out*/;
            inputs["hostInstanceType"] = undefined /*out*/;
            inputs["ipAddresses"] = undefined /*out*/;
            inputs["ldapServerMetadata"] = undefined /*out*/;
            inputs["logs"] = undefined /*out*/;
            inputs["maintenanceWindowStartTime"] = undefined /*out*/;
            inputs["mqttEndpoints"] = undefined /*out*/;
            inputs["openWireEndpoints"] = undefined /*out*/;
            inputs["publiclyAccessible"] = undefined /*out*/;
            inputs["securityGroups"] = undefined /*out*/;
            inputs["stompEndpoints"] = undefined /*out*/;
            inputs["storageType"] = undefined /*out*/;
            inputs["subnetIds"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["users"] = undefined /*out*/;
            inputs["wssEndpoints"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Broker.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Broker resource.
 */
export interface BrokerArgs {
    authenticationStrategy?: pulumi.Input<string>;
    autoMinorVersionUpgrade: pulumi.Input<boolean>;
    brokerName: pulumi.Input<string>;
    configuration?: pulumi.Input<inputs.amazonmq.BrokerConfigurationIdArgs>;
    deploymentMode: pulumi.Input<string>;
    encryptionOptions?: pulumi.Input<inputs.amazonmq.BrokerEncryptionOptionsArgs>;
    engineType: pulumi.Input<string>;
    engineVersion: pulumi.Input<string>;
    hostInstanceType: pulumi.Input<string>;
    ldapServerMetadata?: pulumi.Input<inputs.amazonmq.BrokerLdapServerMetadataArgs>;
    logs?: pulumi.Input<inputs.amazonmq.BrokerLogListArgs>;
    maintenanceWindowStartTime?: pulumi.Input<inputs.amazonmq.BrokerMaintenanceWindowArgs>;
    publiclyAccessible: pulumi.Input<boolean>;
    securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
    storageType?: pulumi.Input<string>;
    subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
    tags?: pulumi.Input<pulumi.Input<inputs.amazonmq.BrokerTagsEntryArgs>[]>;
    users: pulumi.Input<pulumi.Input<inputs.amazonmq.BrokerUserArgs>[]>;
}
