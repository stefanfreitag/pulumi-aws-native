// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SSM::PatchBaseline
 */
export class PatchBaseline extends pulumi.CustomResource {
    /**
     * Get an existing PatchBaseline resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): PatchBaseline {
        return new PatchBaseline(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ssm:PatchBaseline';

    /**
     * Returns true if the given object is an instance of PatchBaseline.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PatchBaseline {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PatchBaseline.__pulumiType;
    }

    public readonly approvalRules!: pulumi.Output<outputs.ssm.PatchBaselineRuleGroup | undefined>;
    /**
     * A list of explicitly approved patches for the baseline.
     */
    public readonly approvedPatches!: pulumi.Output<string[] | undefined>;
    /**
     * Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. The default value is UNSPECIFIED.
     */
    public readonly approvedPatchesComplianceLevel!: pulumi.Output<enums.ssm.PatchBaselineApprovedPatchesComplianceLevel | undefined>;
    /**
     * Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. The default value is 'false'. Applies to Linux instances only.
     */
    public readonly approvedPatchesEnableNonSecurity!: pulumi.Output<boolean | undefined>;
    /**
     * Set the baseline as default baseline. Only registering to default patch baseline is allowed.
     */
    public readonly defaultBaseline!: pulumi.Output<boolean | undefined>;
    /**
     * The description of the patch baseline.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * A set of global filters used to include patches in the baseline.
     */
    public readonly globalFilters!: pulumi.Output<outputs.ssm.PatchBaselinePatchFilterGroup | undefined>;
    /**
     * The name of the patch baseline.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Defines the operating system the patch baseline applies to. The Default value is WINDOWS.
     */
    public readonly operatingSystem!: pulumi.Output<enums.ssm.PatchBaselineOperatingSystem | undefined>;
    /**
     * PatchGroups is used to associate instances with a specific patch baseline
     */
    public readonly patchGroups!: pulumi.Output<string[] | undefined>;
    /**
     * A list of explicitly rejected patches for the baseline.
     */
    public readonly rejectedPatches!: pulumi.Output<string[] | undefined>;
    /**
     * The action for Patch Manager to take on patches included in the RejectedPackages list.
     */
    public readonly rejectedPatchesAction!: pulumi.Output<enums.ssm.PatchBaselineRejectedPatchesAction | undefined>;
    /**
     * Information about the patches to use to update the instances, including target operating systems and source repository. Applies to Linux instances only.
     */
    public readonly sources!: pulumi.Output<outputs.ssm.PatchBaselinePatchSource[] | undefined>;
    /**
     * Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways.
     */
    public readonly tags!: pulumi.Output<outputs.ssm.PatchBaselineTag[] | undefined>;

    /**
     * Create a PatchBaseline resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: PatchBaselineArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["approvalRules"] = args ? args.approvalRules : undefined;
            resourceInputs["approvedPatches"] = args ? args.approvedPatches : undefined;
            resourceInputs["approvedPatchesComplianceLevel"] = args ? args.approvedPatchesComplianceLevel : undefined;
            resourceInputs["approvedPatchesEnableNonSecurity"] = args ? args.approvedPatchesEnableNonSecurity : undefined;
            resourceInputs["defaultBaseline"] = args ? args.defaultBaseline : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["globalFilters"] = args ? args.globalFilters : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["operatingSystem"] = args ? args.operatingSystem : undefined;
            resourceInputs["patchGroups"] = args ? args.patchGroups : undefined;
            resourceInputs["rejectedPatches"] = args ? args.rejectedPatches : undefined;
            resourceInputs["rejectedPatchesAction"] = args ? args.rejectedPatchesAction : undefined;
            resourceInputs["sources"] = args ? args.sources : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        } else {
            resourceInputs["approvalRules"] = undefined /*out*/;
            resourceInputs["approvedPatches"] = undefined /*out*/;
            resourceInputs["approvedPatchesComplianceLevel"] = undefined /*out*/;
            resourceInputs["approvedPatchesEnableNonSecurity"] = undefined /*out*/;
            resourceInputs["defaultBaseline"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["globalFilters"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["operatingSystem"] = undefined /*out*/;
            resourceInputs["patchGroups"] = undefined /*out*/;
            resourceInputs["rejectedPatches"] = undefined /*out*/;
            resourceInputs["rejectedPatchesAction"] = undefined /*out*/;
            resourceInputs["sources"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["operatingSystem"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(PatchBaseline.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a PatchBaseline resource.
 */
export interface PatchBaselineArgs {
    approvalRules?: pulumi.Input<inputs.ssm.PatchBaselineRuleGroupArgs>;
    /**
     * A list of explicitly approved patches for the baseline.
     */
    approvedPatches?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. The default value is UNSPECIFIED.
     */
    approvedPatchesComplianceLevel?: pulumi.Input<enums.ssm.PatchBaselineApprovedPatchesComplianceLevel>;
    /**
     * Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. The default value is 'false'. Applies to Linux instances only.
     */
    approvedPatchesEnableNonSecurity?: pulumi.Input<boolean>;
    /**
     * Set the baseline as default baseline. Only registering to default patch baseline is allowed.
     */
    defaultBaseline?: pulumi.Input<boolean>;
    /**
     * The description of the patch baseline.
     */
    description?: pulumi.Input<string>;
    /**
     * A set of global filters used to include patches in the baseline.
     */
    globalFilters?: pulumi.Input<inputs.ssm.PatchBaselinePatchFilterGroupArgs>;
    /**
     * The name of the patch baseline.
     */
    name?: pulumi.Input<string>;
    /**
     * Defines the operating system the patch baseline applies to. The Default value is WINDOWS.
     */
    operatingSystem?: pulumi.Input<enums.ssm.PatchBaselineOperatingSystem>;
    /**
     * PatchGroups is used to associate instances with a specific patch baseline
     */
    patchGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of explicitly rejected patches for the baseline.
     */
    rejectedPatches?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The action for Patch Manager to take on patches included in the RejectedPackages list.
     */
    rejectedPatchesAction?: pulumi.Input<enums.ssm.PatchBaselineRejectedPatchesAction>;
    /**
     * Information about the patches to use to update the instances, including target operating systems and source repository. Applies to Linux instances only.
     */
    sources?: pulumi.Input<pulumi.Input<inputs.ssm.PatchBaselinePatchSourceArgs>[]>;
    /**
     * Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.ssm.PatchBaselineTagArgs>[]>;
}
