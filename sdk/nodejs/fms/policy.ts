// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Creates an AWS Firewall Manager policy.
 */
export class Policy extends pulumi.CustomResource {
    /**
     * Get an existing Policy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Policy {
        return new Policy(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:fms:Policy';

    /**
     * Returns true if the given object is an instance of Policy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Policy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Policy.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly deleteAllPolicyResources!: pulumi.Output<boolean | undefined>;
    public readonly excludeMap!: pulumi.Output<outputs.fms.PolicyIeMap | undefined>;
    public readonly excludeResourceTags!: pulumi.Output<boolean>;
    public readonly includeMap!: pulumi.Output<outputs.fms.PolicyIeMap | undefined>;
    public readonly policyDescription!: pulumi.Output<string | undefined>;
    public readonly policyName!: pulumi.Output<string>;
    public readonly remediationEnabled!: pulumi.Output<boolean>;
    public readonly resourceSetIds!: pulumi.Output<string[] | undefined>;
    public readonly resourceTags!: pulumi.Output<outputs.fms.PolicyResourceTag[] | undefined>;
    public readonly resourceType!: pulumi.Output<string | undefined>;
    public readonly resourceTypeList!: pulumi.Output<string[] | undefined>;
    public readonly resourcesCleanUp!: pulumi.Output<boolean | undefined>;
    public readonly securityServicePolicyData!: pulumi.Output<outputs.fms.PolicySecurityServicePolicyData>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a Policy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PolicyArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.excludeResourceTags === undefined) && !opts.urn) {
                throw new Error("Missing required property 'excludeResourceTags'");
            }
            if ((!args || args.remediationEnabled === undefined) && !opts.urn) {
                throw new Error("Missing required property 'remediationEnabled'");
            }
            if ((!args || args.securityServicePolicyData === undefined) && !opts.urn) {
                throw new Error("Missing required property 'securityServicePolicyData'");
            }
            resourceInputs["deleteAllPolicyResources"] = args ? args.deleteAllPolicyResources : undefined;
            resourceInputs["excludeMap"] = args ? args.excludeMap : undefined;
            resourceInputs["excludeResourceTags"] = args ? args.excludeResourceTags : undefined;
            resourceInputs["includeMap"] = args ? args.includeMap : undefined;
            resourceInputs["policyDescription"] = args ? args.policyDescription : undefined;
            resourceInputs["policyName"] = args ? args.policyName : undefined;
            resourceInputs["remediationEnabled"] = args ? args.remediationEnabled : undefined;
            resourceInputs["resourceSetIds"] = args ? args.resourceSetIds : undefined;
            resourceInputs["resourceTags"] = args ? args.resourceTags : undefined;
            resourceInputs["resourceType"] = args ? args.resourceType : undefined;
            resourceInputs["resourceTypeList"] = args ? args.resourceTypeList : undefined;
            resourceInputs["resourcesCleanUp"] = args ? args.resourcesCleanUp : undefined;
            resourceInputs["securityServicePolicyData"] = args ? args.securityServicePolicyData : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["deleteAllPolicyResources"] = undefined /*out*/;
            resourceInputs["excludeMap"] = undefined /*out*/;
            resourceInputs["excludeResourceTags"] = undefined /*out*/;
            resourceInputs["includeMap"] = undefined /*out*/;
            resourceInputs["policyDescription"] = undefined /*out*/;
            resourceInputs["policyName"] = undefined /*out*/;
            resourceInputs["remediationEnabled"] = undefined /*out*/;
            resourceInputs["resourceSetIds"] = undefined /*out*/;
            resourceInputs["resourceTags"] = undefined /*out*/;
            resourceInputs["resourceType"] = undefined /*out*/;
            resourceInputs["resourceTypeList"] = undefined /*out*/;
            resourceInputs["resourcesCleanUp"] = undefined /*out*/;
            resourceInputs["securityServicePolicyData"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Policy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Policy resource.
 */
export interface PolicyArgs {
    deleteAllPolicyResources?: pulumi.Input<boolean>;
    excludeMap?: pulumi.Input<inputs.fms.PolicyIeMapArgs>;
    excludeResourceTags: pulumi.Input<boolean>;
    includeMap?: pulumi.Input<inputs.fms.PolicyIeMapArgs>;
    policyDescription?: pulumi.Input<string>;
    policyName?: pulumi.Input<string>;
    remediationEnabled: pulumi.Input<boolean>;
    resourceSetIds?: pulumi.Input<pulumi.Input<string>[]>;
    resourceTags?: pulumi.Input<pulumi.Input<inputs.fms.PolicyResourceTagArgs>[]>;
    resourceType?: pulumi.Input<string>;
    resourceTypeList?: pulumi.Input<pulumi.Input<string>[]>;
    resourcesCleanUp?: pulumi.Input<boolean>;
    securityServicePolicyData: pulumi.Input<inputs.fms.PolicySecurityServicePolicyDataArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
