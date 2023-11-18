// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The AWS::ECR::PullThroughCacheRule resource configures the upstream registry configuration details for an Amazon Elastic Container Registry (Amazon Private ECR) pull-through cache.
 */
export class PullThroughCacheRule extends pulumi.CustomResource {
    /**
     * Get an existing PullThroughCacheRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): PullThroughCacheRule {
        return new PullThroughCacheRule(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ecr:PullThroughCacheRule';

    /**
     * Returns true if the given object is an instance of PullThroughCacheRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PullThroughCacheRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PullThroughCacheRule.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.
     */
    public readonly credentialArn!: pulumi.Output<string | undefined>;
    /**
     * The ECRRepositoryPrefix is a custom alias for upstream registry url.
     */
    public readonly ecrRepositoryPrefix!: pulumi.Output<string | undefined>;
    /**
     * The name of the upstream registry.
     */
    public readonly upstreamRegistry!: pulumi.Output<string | undefined>;
    /**
     * The upstreamRegistryUrl is the endpoint of upstream registry url of the public repository to be cached
     */
    public readonly upstreamRegistryUrl!: pulumi.Output<string | undefined>;

    /**
     * Create a PullThroughCacheRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: PullThroughCacheRuleArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["credentialArn"] = args ? args.credentialArn : undefined;
            resourceInputs["ecrRepositoryPrefix"] = args ? args.ecrRepositoryPrefix : undefined;
            resourceInputs["upstreamRegistry"] = args ? args.upstreamRegistry : undefined;
            resourceInputs["upstreamRegistryUrl"] = args ? args.upstreamRegistryUrl : undefined;
        } else {
            resourceInputs["credentialArn"] = undefined /*out*/;
            resourceInputs["ecrRepositoryPrefix"] = undefined /*out*/;
            resourceInputs["upstreamRegistry"] = undefined /*out*/;
            resourceInputs["upstreamRegistryUrl"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["credentialArn", "ecrRepositoryPrefix", "upstreamRegistry", "upstreamRegistryUrl"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(PullThroughCacheRule.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a PullThroughCacheRule resource.
 */
export interface PullThroughCacheRuleArgs {
    /**
     * The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.
     */
    credentialArn?: pulumi.Input<string>;
    /**
     * The ECRRepositoryPrefix is a custom alias for upstream registry url.
     */
    ecrRepositoryPrefix?: pulumi.Input<string>;
    /**
     * The name of the upstream registry.
     */
    upstreamRegistry?: pulumi.Input<string>;
    /**
     * The upstreamRegistryUrl is the endpoint of upstream registry url of the public repository to be cached
     */
    upstreamRegistryUrl?: pulumi.Input<string>;
}
