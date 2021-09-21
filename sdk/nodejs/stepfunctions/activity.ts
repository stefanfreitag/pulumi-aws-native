// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::StepFunctions::Activity
 *
 * @deprecated Activity is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Activity extends pulumi.CustomResource {
    /**
     * Get an existing Activity resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Activity {
        pulumi.log.warn("Activity is deprecated: Activity is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Activity(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:stepfunctions:Activity';

    /**
     * Returns true if the given object is an instance of Activity.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Activity {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Activity.__pulumiType;
    }

    public readonly name!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.stepfunctions.ActivityTagsEntry[] | undefined>;

    /**
     * Create a Activity resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Activity is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ActivityArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Activity is deprecated: Activity is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
        } else {
            inputs["name"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Activity.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Activity resource.
 */
export interface ActivityArgs {
    name: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.stepfunctions.ActivityTagsEntryArgs>[]>;
}
