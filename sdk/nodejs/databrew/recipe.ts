// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::DataBrew::Recipe.
 */
export class Recipe extends pulumi.CustomResource {
    /**
     * Get an existing Recipe resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Recipe {
        return new Recipe(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:databrew:Recipe';

    /**
     * Returns true if the given object is an instance of Recipe.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Recipe {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Recipe.__pulumiType;
    }

    /**
     * Description of the recipe
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Recipe name
     */
    public readonly name!: pulumi.Output<string>;
    public readonly steps!: pulumi.Output<outputs.databrew.RecipeStep[]>;
    public readonly tags!: pulumi.Output<outputs.CreateOnlyTag[] | undefined>;

    /**
     * Create a Recipe resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RecipeArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.steps === undefined) && !opts.urn) {
                throw new Error("Missing required property 'steps'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["steps"] = args ? args.steps : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        } else {
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["steps"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name", "tags[*]"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Recipe.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Recipe resource.
 */
export interface RecipeArgs {
    /**
     * Description of the recipe
     */
    description?: pulumi.Input<string>;
    /**
     * Recipe name
     */
    name?: pulumi.Input<string>;
    steps: pulumi.Input<pulumi.Input<inputs.databrew.RecipeStepArgs>[]>;
    tags?: pulumi.Input<pulumi.Input<inputs.CreateOnlyTagArgs>[]>;
}
