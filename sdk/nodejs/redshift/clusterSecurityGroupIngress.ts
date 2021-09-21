// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Redshift::ClusterSecurityGroupIngress
 *
 * @deprecated ClusterSecurityGroupIngress is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class ClusterSecurityGroupIngress extends pulumi.CustomResource {
    /**
     * Get an existing ClusterSecurityGroupIngress resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ClusterSecurityGroupIngress {
        pulumi.log.warn("ClusterSecurityGroupIngress is deprecated: ClusterSecurityGroupIngress is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new ClusterSecurityGroupIngress(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:redshift:ClusterSecurityGroupIngress';

    /**
     * Returns true if the given object is an instance of ClusterSecurityGroupIngress.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ClusterSecurityGroupIngress {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ClusterSecurityGroupIngress.__pulumiType;
    }

    public readonly cIDRIP!: pulumi.Output<string | undefined>;
    public readonly clusterSecurityGroupName!: pulumi.Output<string>;
    public readonly eC2SecurityGroupName!: pulumi.Output<string | undefined>;
    public readonly eC2SecurityGroupOwnerId!: pulumi.Output<string | undefined>;

    /**
     * Create a ClusterSecurityGroupIngress resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated ClusterSecurityGroupIngress is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ClusterSecurityGroupIngressArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("ClusterSecurityGroupIngress is deprecated: ClusterSecurityGroupIngress is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.clusterSecurityGroupName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterSecurityGroupName'");
            }
            inputs["cIDRIP"] = args ? args.cIDRIP : undefined;
            inputs["clusterSecurityGroupName"] = args ? args.clusterSecurityGroupName : undefined;
            inputs["eC2SecurityGroupName"] = args ? args.eC2SecurityGroupName : undefined;
            inputs["eC2SecurityGroupOwnerId"] = args ? args.eC2SecurityGroupOwnerId : undefined;
        } else {
            inputs["cIDRIP"] = undefined /*out*/;
            inputs["clusterSecurityGroupName"] = undefined /*out*/;
            inputs["eC2SecurityGroupName"] = undefined /*out*/;
            inputs["eC2SecurityGroupOwnerId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ClusterSecurityGroupIngress.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ClusterSecurityGroupIngress resource.
 */
export interface ClusterSecurityGroupIngressArgs {
    cIDRIP?: pulumi.Input<string>;
    clusterSecurityGroupName: pulumi.Input<string>;
    eC2SecurityGroupName?: pulumi.Input<string>;
    eC2SecurityGroupOwnerId?: pulumi.Input<string>;
}
