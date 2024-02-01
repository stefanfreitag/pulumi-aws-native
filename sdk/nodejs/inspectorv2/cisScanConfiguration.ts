// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * CIS Scan Configuration resource schema
 */
export class CisScanConfiguration extends pulumi.CustomResource {
    /**
     * Get an existing CisScanConfiguration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): CisScanConfiguration {
        return new CisScanConfiguration(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:inspectorv2:CisScanConfiguration';

    /**
     * Returns true if the given object is an instance of CisScanConfiguration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CisScanConfiguration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CisScanConfiguration.__pulumiType;
    }

    /**
     * CIS Scan configuration unique identifier
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Name of the scan
     */
    public readonly scanName!: pulumi.Output<string | undefined>;
    public readonly schedule!: pulumi.Output<outputs.inspectorv2.CisScanConfigurationSchedule | undefined>;
    public readonly securityLevel!: pulumi.Output<enums.inspectorv2.CisScanConfigurationCisSecurityLevel | undefined>;
    public readonly tags!: pulumi.Output<outputs.inspectorv2.CisScanConfigurationCisTagMap | undefined>;
    public readonly targets!: pulumi.Output<outputs.inspectorv2.CisScanConfigurationCisTargets | undefined>;

    /**
     * Create a CisScanConfiguration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: CisScanConfigurationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["scanName"] = args ? args.scanName : undefined;
            resourceInputs["schedule"] = args ? args.schedule : undefined;
            resourceInputs["securityLevel"] = args ? args.securityLevel : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["targets"] = args ? args.targets : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["scanName"] = undefined /*out*/;
            resourceInputs["schedule"] = undefined /*out*/;
            resourceInputs["securityLevel"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["targets"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(CisScanConfiguration.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a CisScanConfiguration resource.
 */
export interface CisScanConfigurationArgs {
    /**
     * Name of the scan
     */
    scanName?: pulumi.Input<string>;
    schedule?: pulumi.Input<inputs.inspectorv2.CisScanConfigurationScheduleArgs>;
    securityLevel?: pulumi.Input<enums.inspectorv2.CisScanConfigurationCisSecurityLevel>;
    tags?: pulumi.Input<inputs.inspectorv2.CisScanConfigurationCisTagMapArgs>;
    targets?: pulumi.Input<inputs.inspectorv2.CisScanConfigurationCisTargetsArgs>;
}
