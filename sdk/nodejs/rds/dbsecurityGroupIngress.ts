// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::RDS::DBSecurityGroupIngress
 *
 * @deprecated DBSecurityGroupIngress is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class DBSecurityGroupIngress extends pulumi.CustomResource {
    /**
     * Get an existing DBSecurityGroupIngress resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DBSecurityGroupIngress {
        pulumi.log.warn("DBSecurityGroupIngress is deprecated: DBSecurityGroupIngress is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new DBSecurityGroupIngress(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:rds:DBSecurityGroupIngress';

    /**
     * Returns true if the given object is an instance of DBSecurityGroupIngress.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DBSecurityGroupIngress {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DBSecurityGroupIngress.__pulumiType;
    }

    public readonly cIDRIP!: pulumi.Output<string | undefined>;
    public readonly dBSecurityGroupName!: pulumi.Output<string>;
    public readonly eC2SecurityGroupId!: pulumi.Output<string | undefined>;
    public readonly eC2SecurityGroupName!: pulumi.Output<string | undefined>;
    public readonly eC2SecurityGroupOwnerId!: pulumi.Output<string | undefined>;

    /**
     * Create a DBSecurityGroupIngress resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated DBSecurityGroupIngress is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: DBSecurityGroupIngressArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("DBSecurityGroupIngress is deprecated: DBSecurityGroupIngress is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.dBSecurityGroupName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dBSecurityGroupName'");
            }
            inputs["cIDRIP"] = args ? args.cIDRIP : undefined;
            inputs["dBSecurityGroupName"] = args ? args.dBSecurityGroupName : undefined;
            inputs["eC2SecurityGroupId"] = args ? args.eC2SecurityGroupId : undefined;
            inputs["eC2SecurityGroupName"] = args ? args.eC2SecurityGroupName : undefined;
            inputs["eC2SecurityGroupOwnerId"] = args ? args.eC2SecurityGroupOwnerId : undefined;
        } else {
            inputs["cIDRIP"] = undefined /*out*/;
            inputs["dBSecurityGroupName"] = undefined /*out*/;
            inputs["eC2SecurityGroupId"] = undefined /*out*/;
            inputs["eC2SecurityGroupName"] = undefined /*out*/;
            inputs["eC2SecurityGroupOwnerId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(DBSecurityGroupIngress.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a DBSecurityGroupIngress resource.
 */
export interface DBSecurityGroupIngressArgs {
    cIDRIP?: pulumi.Input<string>;
    dBSecurityGroupName: pulumi.Input<string>;
    eC2SecurityGroupId?: pulumi.Input<string>;
    eC2SecurityGroupName?: pulumi.Input<string>;
    eC2SecurityGroupOwnerId?: pulumi.Input<string>;
}
