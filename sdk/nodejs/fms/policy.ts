// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
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
    public readonly excludeMap!: pulumi.Output<outputs.fms.PolicyIEMap | undefined>;
    public readonly excludeResourceTags!: pulumi.Output<boolean>;
    public readonly includeMap!: pulumi.Output<outputs.fms.PolicyIEMap | undefined>;
    public readonly policyName!: pulumi.Output<string>;
    public readonly remediationEnabled!: pulumi.Output<boolean>;
    public readonly resourceTags!: pulumi.Output<outputs.fms.PolicyResourceTag[] | undefined>;
    public readonly resourceType!: pulumi.Output<string>;
    public readonly resourceTypeList!: pulumi.Output<string[] | undefined>;
    public readonly securityServicePolicyData!: pulumi.Output<any>;
    public readonly tags!: pulumi.Output<outputs.fms.PolicyPolicyTag[] | undefined>;

    /**
     * Create a Policy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PolicyArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.excludeResourceTags === undefined) && !opts.urn) {
                throw new Error("Missing required property 'excludeResourceTags'");
            }
            if ((!args || args.policyName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'policyName'");
            }
            if ((!args || args.remediationEnabled === undefined) && !opts.urn) {
                throw new Error("Missing required property 'remediationEnabled'");
            }
            if ((!args || args.resourceType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceType'");
            }
            if ((!args || args.securityServicePolicyData === undefined) && !opts.urn) {
                throw new Error("Missing required property 'securityServicePolicyData'");
            }
            inputs["deleteAllPolicyResources"] = args ? args.deleteAllPolicyResources : undefined;
            inputs["excludeMap"] = args ? args.excludeMap : undefined;
            inputs["excludeResourceTags"] = args ? args.excludeResourceTags : undefined;
            inputs["includeMap"] = args ? args.includeMap : undefined;
            inputs["policyName"] = args ? args.policyName : undefined;
            inputs["remediationEnabled"] = args ? args.remediationEnabled : undefined;
            inputs["resourceTags"] = args ? args.resourceTags : undefined;
            inputs["resourceType"] = args ? args.resourceType : undefined;
            inputs["resourceTypeList"] = args ? args.resourceTypeList : undefined;
            inputs["securityServicePolicyData"] = args ? args.securityServicePolicyData : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["deleteAllPolicyResources"] = undefined /*out*/;
            inputs["excludeMap"] = undefined /*out*/;
            inputs["excludeResourceTags"] = undefined /*out*/;
            inputs["includeMap"] = undefined /*out*/;
            inputs["policyName"] = undefined /*out*/;
            inputs["remediationEnabled"] = undefined /*out*/;
            inputs["resourceTags"] = undefined /*out*/;
            inputs["resourceType"] = undefined /*out*/;
            inputs["resourceTypeList"] = undefined /*out*/;
            inputs["securityServicePolicyData"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Policy.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Policy resource.
 */
export interface PolicyArgs {
    deleteAllPolicyResources?: pulumi.Input<boolean>;
    excludeMap?: pulumi.Input<inputs.fms.PolicyIEMapArgs>;
    excludeResourceTags: pulumi.Input<boolean>;
    includeMap?: pulumi.Input<inputs.fms.PolicyIEMapArgs>;
    policyName: pulumi.Input<string>;
    remediationEnabled: pulumi.Input<boolean>;
    resourceTags?: pulumi.Input<pulumi.Input<inputs.fms.PolicyResourceTagArgs>[]>;
    resourceType: pulumi.Input<string>;
    resourceTypeList?: pulumi.Input<pulumi.Input<string>[]>;
    securityServicePolicyData: any;
    tags?: pulumi.Input<pulumi.Input<inputs.fms.PolicyPolicyTagArgs>[]>;
}
