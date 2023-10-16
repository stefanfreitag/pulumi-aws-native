// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * An object representing an Amazon EKS cluster.
 */
export class Cluster extends pulumi.CustomResource {
    /**
     * Get an existing Cluster resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Cluster {
        return new Cluster(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:eks:Cluster';

    /**
     * Returns true if the given object is an instance of Cluster.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Cluster {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Cluster.__pulumiType;
    }

    /**
     * The ARN of the cluster, such as arn:aws:eks:us-west-2:666666666666:cluster/prod.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The certificate-authority-data for your cluster.
     */
    public /*out*/ readonly certificateAuthorityData!: pulumi.Output<string>;
    /**
     * The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control plane to data plane communication.
     */
    public /*out*/ readonly clusterSecurityGroupId!: pulumi.Output<string>;
    public readonly encryptionConfig!: pulumi.Output<outputs.eks.ClusterEncryptionConfig[] | undefined>;
    /**
     * Amazon Resource Name (ARN) or alias of the customer master key (CMK).
     */
    public /*out*/ readonly encryptionConfigKeyArn!: pulumi.Output<string>;
    /**
     * The endpoint for your Kubernetes API server, such as https://5E1D0CEXAMPLEA591B746AFC5AB30262.yl4.us-west-2.eks.amazonaws.com.
     */
    public /*out*/ readonly endpoint!: pulumi.Output<string>;
    public readonly kubernetesNetworkConfig!: pulumi.Output<outputs.eks.ClusterKubernetesNetworkConfig | undefined>;
    public readonly logging!: pulumi.Output<outputs.eks.Logging | undefined>;
    /**
     * The unique name to give to your cluster.
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * The issuer URL for the cluster's OIDC identity provider, such as https://oidc.eks.us-west-2.amazonaws.com/id/EXAMPLED539D4633E53DE1B716D3041E. If you need to remove https:// from this output value, you can include the following code in your template.
     */
    public /*out*/ readonly openIdConnectIssuerUrl!: pulumi.Output<string>;
    public readonly outpostConfig!: pulumi.Output<outputs.eks.ClusterOutpostConfig | undefined>;
    public readonly resourcesVpcConfig!: pulumi.Output<outputs.eks.ClusterResourcesVpcConfig>;
    /**
     * The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
     */
    public readonly roleArn!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.eks.ClusterTag[] | undefined>;
    /**
     * The desired Kubernetes version for your cluster. If you don't specify a value here, the latest version available in Amazon EKS is used.
     */
    public readonly version!: pulumi.Output<string | undefined>;

    /**
     * Create a Cluster resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ClusterArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.resourcesVpcConfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourcesVpcConfig'");
            }
            if ((!args || args.roleArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'roleArn'");
            }
            resourceInputs["encryptionConfig"] = args ? args.encryptionConfig : undefined;
            resourceInputs["kubernetesNetworkConfig"] = args ? args.kubernetesNetworkConfig : undefined;
            resourceInputs["logging"] = args ? args.logging : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["outpostConfig"] = args ? args.outpostConfig : undefined;
            resourceInputs["resourcesVpcConfig"] = args ? args.resourcesVpcConfig : undefined;
            resourceInputs["roleArn"] = args ? args.roleArn : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["version"] = args ? args.version : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["certificateAuthorityData"] = undefined /*out*/;
            resourceInputs["clusterSecurityGroupId"] = undefined /*out*/;
            resourceInputs["encryptionConfigKeyArn"] = undefined /*out*/;
            resourceInputs["endpoint"] = undefined /*out*/;
            resourceInputs["openIdConnectIssuerUrl"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["certificateAuthorityData"] = undefined /*out*/;
            resourceInputs["clusterSecurityGroupId"] = undefined /*out*/;
            resourceInputs["encryptionConfig"] = undefined /*out*/;
            resourceInputs["encryptionConfigKeyArn"] = undefined /*out*/;
            resourceInputs["endpoint"] = undefined /*out*/;
            resourceInputs["kubernetesNetworkConfig"] = undefined /*out*/;
            resourceInputs["logging"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["openIdConnectIssuerUrl"] = undefined /*out*/;
            resourceInputs["outpostConfig"] = undefined /*out*/;
            resourceInputs["resourcesVpcConfig"] = undefined /*out*/;
            resourceInputs["roleArn"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["version"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["encryptionConfig[*]", "kubernetesNetworkConfig", "name", "outpostConfig", "roleArn"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Cluster.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Cluster resource.
 */
export interface ClusterArgs {
    encryptionConfig?: pulumi.Input<pulumi.Input<inputs.eks.ClusterEncryptionConfigArgs>[]>;
    kubernetesNetworkConfig?: pulumi.Input<inputs.eks.ClusterKubernetesNetworkConfigArgs>;
    logging?: pulumi.Input<inputs.eks.LoggingArgs>;
    /**
     * The unique name to give to your cluster.
     */
    name?: pulumi.Input<string>;
    outpostConfig?: pulumi.Input<inputs.eks.ClusterOutpostConfigArgs>;
    resourcesVpcConfig: pulumi.Input<inputs.eks.ClusterResourcesVpcConfigArgs>;
    /**
     * The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
     */
    roleArn: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.eks.ClusterTagArgs>[]>;
    /**
     * The desired Kubernetes version for your cluster. If you don't specify a value here, the latest version available in Amazon EKS is used.
     */
    version?: pulumi.Input<string>;
}
