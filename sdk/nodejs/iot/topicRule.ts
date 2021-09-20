// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::IoT::TopicRule
 */
export class TopicRule extends pulumi.CustomResource {
    /**
     * Get an existing TopicRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): TopicRule {
        return new TopicRule(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iot:TopicRule';

    /**
     * Returns true if the given object is an instance of TopicRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TopicRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TopicRule.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly ruleName!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.iot.TopicRuleTag[] | undefined>;
    public readonly topicRulePayload!: pulumi.Output<outputs.iot.TopicRuleTopicRulePayload>;

    /**
     * Create a TopicRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TopicRuleArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.topicRulePayload === undefined) && !opts.urn) {
                throw new Error("Missing required property 'topicRulePayload'");
            }
            inputs["ruleName"] = args ? args.ruleName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["topicRulePayload"] = args ? args.topicRulePayload : undefined;
            inputs["arn"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["ruleName"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["topicRulePayload"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(TopicRule.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a TopicRule resource.
 */
export interface TopicRuleArgs {
    ruleName?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.iot.TopicRuleTagArgs>[]>;
    topicRulePayload: pulumi.Input<inputs.iot.TopicRuleTopicRulePayloadArgs>;
}
