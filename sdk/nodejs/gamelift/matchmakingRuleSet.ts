// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::GameLift::MatchmakingRuleSet resource creates an Amazon GameLift (GameLift) matchmaking rule set.
 */
export class MatchmakingRuleSet extends pulumi.CustomResource {
    /**
     * Get an existing MatchmakingRuleSet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): MatchmakingRuleSet {
        return new MatchmakingRuleSet(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:gamelift:MatchmakingRuleSet';

    /**
     * Returns true if the given object is an instance of MatchmakingRuleSet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MatchmakingRuleSet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MatchmakingRuleSet.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift matchmaking rule set resource and uniquely identifies it.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds.
     */
    public /*out*/ readonly creationTime!: pulumi.Output<string>;
    /**
     * A unique identifier for the matchmaking rule set.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A collection of matchmaking rules, formatted as a JSON string.
     */
    public readonly ruleSetBody!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.gamelift.MatchmakingRuleSetTag[] | undefined>;

    /**
     * Create a MatchmakingRuleSet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MatchmakingRuleSetArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.ruleSetBody === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ruleSetBody'");
            }
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["ruleSetBody"] = args ? args.ruleSetBody : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["creationTime"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["ruleSetBody"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name", "ruleSetBody"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(MatchmakingRuleSet.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a MatchmakingRuleSet resource.
 */
export interface MatchmakingRuleSetArgs {
    /**
     * A unique identifier for the matchmaking rule set.
     */
    name?: pulumi.Input<string>;
    /**
     * A collection of matchmaking rules, formatted as a JSON string.
     */
    ruleSetBody: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.gamelift.MatchmakingRuleSetTagArgs>[]>;
}
