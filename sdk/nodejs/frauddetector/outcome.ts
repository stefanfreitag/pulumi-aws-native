// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * An outcome for rule evaluation.
 */
export class Outcome extends pulumi.CustomResource {
    /**
     * Get an existing Outcome resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Outcome {
        return new Outcome(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:frauddetector:Outcome';

    /**
     * Returns true if the given object is an instance of Outcome.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Outcome {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Outcome.__pulumiType;
    }

    /**
     * The outcome ARN.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The timestamp when the outcome was created.
     */
    public /*out*/ readonly createdTime!: pulumi.Output<string>;
    /**
     * The outcome description.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The timestamp when the outcome was last updated.
     */
    public /*out*/ readonly lastUpdatedTime!: pulumi.Output<string>;
    /**
     * The name of the outcome.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Tags associated with this outcome.
     */
    public readonly tags!: pulumi.Output<outputs.frauddetector.OutcomeTag[] | undefined>;

    /**
     * Create a Outcome resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: OutcomeArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["createdTime"] = undefined /*out*/;
            inputs["lastUpdatedTime"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["createdTime"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["lastUpdatedTime"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Outcome.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Outcome resource.
 */
export interface OutcomeArgs {
    /**
     * The outcome description.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the outcome.
     */
    name: pulumi.Input<string>;
    /**
     * Tags associated with this outcome.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.frauddetector.OutcomeTagArgs>[]>;
}
