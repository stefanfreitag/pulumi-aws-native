// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * resource definition
 */
export class SoftwarePackage extends pulumi.CustomResource {
    /**
     * Get an existing SoftwarePackage resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): SoftwarePackage {
        return new SoftwarePackage(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iot:SoftwarePackage';

    /**
     * Returns true if the given object is an instance of SoftwarePackage.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SoftwarePackage {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SoftwarePackage.__pulumiType;
    }

    public readonly description!: pulumi.Output<string | undefined>;
    public /*out*/ readonly packageArn!: pulumi.Output<string>;
    public readonly packageName!: pulumi.Output<string | undefined>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.iot.SoftwarePackageTag[] | undefined>;

    /**
     * Create a SoftwarePackage resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: SoftwarePackageArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["packageName"] = args ? args.packageName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["packageArn"] = undefined /*out*/;
        } else {
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["packageArn"] = undefined /*out*/;
            resourceInputs["packageName"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["packageName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(SoftwarePackage.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a SoftwarePackage resource.
 */
export interface SoftwarePackageArgs {
    description?: pulumi.Input<string>;
    packageName?: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.iot.SoftwarePackageTagArgs>[]>;
}
